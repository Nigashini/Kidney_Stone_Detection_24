import os
import numpy as np
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image  # Make sure to import Image if it's not imported yet

app = Flask(__name__)

# Define upload folder and allowed extensions (optional)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load the model
model = load_model("D:/USERFILE/New folder (3)/kidney_stone_detection_model.h5")

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Predict route for image upload and prediction
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return render_template("index.html", prediction=None)

    file = request.files["image"]
    if file.filename == "":
        return render_template("index.html", prediction=None)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Preprocess the image for prediction
    image = Image.open(filepath).resize((150, 150))
    img = np.expand_dims(np.array(image) / 255.0, axis=0)

    prediction = model.predict(img)[0][0]
    confidence = round(float(prediction), 2)

    # Recommendations based on confidence
    if confidence > 0.85:
        result = {
            "status": "✅ Stone Detected: Yes",
            "severity": "🧪 Severity: High",
            "recommendations": [
                "📌 Visit a urologist **within 1-2 days**",
                "🚰 Drink **3+ liters** of water daily",
                "❌ Avoid oxalate-rich foods (e.g., spinach, chocolate)",
                "🛌 Reduce physical activity & monitor pain"
            ]
        }
    elif confidence > 0.5:
        result = {
            "status": "⚠️ Possible Stone Detected",
            "severity": "🧪 Severity: Moderate",
            "recommendations": [
                "📌 Visit a urologist **within 3 days**",
                "🚰 Increase water intake",
                "❌ Limit sodium & protein-heavy diets",
                "🧪 Consider further imaging or urine test"
            ]
        }
    else:
        result = {
            "status": "❌ No Stone Detected",
            "severity": "🧪 Severity: Low",
            "recommendations": [
                "💧 Maintain hydration (2.5–3L water/day)",
                "🥗 Eat balanced diet low in salt and sugar",
                "👨‍⚕️ Get annual kidney health checkup",
                "📱 Monitor symptoms & avoid self-medication"
            ]
        }

    return render_template("index.html", result=result, filename=file.filename)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
