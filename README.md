# YOLO-Object-Detection-App
<hr>

This project is a web application built using YOLOv8 and Flask for object detection. The app allows users to upload an image, and it will display detected objects, their confidence scores, and the bounding boxes around them. The model has been trained to detect two classes: Cable Tower and Turbine.

## Technologies Used
<hr>

-YOLOv8: The object detection model used for inference.
-Flask: Web framework for creating the API and frontend interface.
-Python: Programming language used for backend logic.
-Google Colab: Used for training the YOLO model.
-GitHub: For version control and code hosting.

## Features
<hr>

-Upload an image via the web interface.
-Get object detection results including confidence scores and bounding boxes.
-View the original uploaded image and the image with bounding boxes drawn around detected objects.

## Installation & Setup
<hr>

### 1.Clone the repository:
git clone https://github.com/your-username/YOLO-Object-Detection-App.git
cd YOLO-Object-Detection-App

### 2.Set up a Python virtual environment: 
python -m venv venv

### 3.Activate the virtual environment:
For Windows: .\venv\Scripts\activate
For macOS/Linux: source venv/bin/activate

### 4.Install required dependencies: 
pip install -r requirements.txt

### 5.Run the Flask app:
python app.py

### 6.Open the app in your browser:
Navigate to http://127.0.0.1:5000/ to access the app.

## How to Use the App
<hr>

1.Upload an image: Select an image file from your system.
2.The app will display:
-The uploaded image.
-The detected objects (e.g., cable tower and turbine).
-Confidence scores for each detected object.
-The image with bounding boxes drawn around the detected objects.

## Classes Detected
<hr>

-Cable Tower
-Turbine

## Model Training
The YOLOv8 model was trained using a custom dataset containing images of cable towers and turbines. The training process was done on Google Colab, and the trained model weights are available in the weights folder.



