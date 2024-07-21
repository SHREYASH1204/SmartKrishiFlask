from flask import Flask, request
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the model
model_path = 'Fertclassifier.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Welcome to the Fertilizer Predictor"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([
        data['Temperature'],
        data['Humidity'],
        data['Moisture'],
        data['Soil Type'],
        data['Crop Type'],
        data['Nitrogen'],
        data['Potassium'],
        data['Phosphorous']
    ]).reshape(1, -1)
    prediction = model.predict(features)
    return {'prediction': prediction[0]}

if __name__ == '__main__':
    app.run(debug=True)
