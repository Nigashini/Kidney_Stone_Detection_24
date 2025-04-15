# Kidney_Stone_Detection_24
# 🧠 Kidney Stone Detection Using Deep Learning

This project uses a trained **ResNet-50 model** to detect the presence of kidney stones from medical images. It features a user-friendly **Flask web application** for image upload, prediction, and doctor feedback.

## 📌 Features
- Upload CT/ultrasound images of kidneys
- Detect kidney stone presence using deep learning
- Confidence-based severity interpretation and recommendations
- Doctors can submit feedback
- Built-in feedback storage
- Clean Bootstrap-based user interface

## 🛠 Technologies Used
- Python, Flask
- TensorFlow (ResNet-50)
- OpenCV & Pillow for image processing
- HTML/CSS (Bootstrap 5)

## 🚀 How to Run
1. Clone the repository
2. Install dependencies:
3. Run the app:
4.  Open browser at `http://127.0.0.1:5000/`
# # 📂 Project Structure
kidney_stone_app/ 
├── app.py
├── templates/ 
│ └── index.html 
├── static/
│ └── uploads/ 
├── kidney_stone_detection_model.h5
└── README.md

## ✅ Results
- Achieved ~92% accuracy on kidney stone classification
- Deployed with a simple and informative UI
