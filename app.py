from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image, ImageDraw
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/output'  
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = YOLO('weights/best.pt')  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    results = model(image_path)
    detections = results[0].boxes 
    response = []

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    for box in detections:
        x1, y1, x2, y2 = box.xyxy[0].tolist()  
        conf = box.conf[0] 
        cls = int(box.cls[0])  
        label = results[0].names[cls] 
        
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
        draw.text((x1, y1), f"{label} {conf:.2f}", fill="red")
        
        response.append({
            'label': label,
            'confidence': float(conf),
            'box': [x1, y1, x2, y2]
        })

    output_image_path = os.path.join(OUTPUT_FOLDER, file.filename)
    image.save(output_image_path)
    
    uploaded_image_url = f'uploads/{file.filename}'
    output_image_url = f'output/{file.filename}'

    return render_template('index.html', detections=response, uploaded_image_path=uploaded_image_url, output_image_path=output_image_url)

if __name__ == '__main__':
    app.run(debug=True)
