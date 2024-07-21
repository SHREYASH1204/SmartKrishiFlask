# SmartKrishiFlask

SmartKrishiFlask is a web application that leverages a machine learning model to predict the appropriate fertilizer for crops based on various input parameters. This application is built using Flask, a lightweight WSGI web application framework in Python.

## Features

- Load and utilize a pre-trained machine learning model (`Fertclassifier.pkl`).
- API endpoint to predict the appropriate fertilizer based on input parameters.
- CORS support enabled for all routes.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/SHREYASH1204/SmartKrishiFlask.git
    cd SmartKrishiFlask
    ```

2. Create a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r Requirements.txt
    ```

### Running the Application

1. Ensure the model file (`Fertclassifier.pkl`) is present in the root directory.

2. Run the Flask application:

    ```sh
    python app.py
    ```

3. The application will start on `http://127.0.0.1:5000/`. You can access the API endpoint for predictions at `http://127.0.0.1:5000/predict`.

## API Usage

### Predict Endpoint

- **URL:** `/predict`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Request Payload

The JSON payload should contain the following fields:

- `Temperature`: (float) The temperature value.
- `Humidity`: (float) The humidity value.
- `Moisture`: (float) The moisture value.
- `Soil Type`: (int) Encoded value representing the soil type.
- `Crop Type`: (int) Encoded value representing the crop type.
- `Nitrogen`: (float) Nitrogen content.
- `Potassium`: (float) Potassium content.
- `Phosphorous`: (float) Phosphorous content.

Example:

```json
{
    "Temperature": 23.5,
    "Humidity": 85,
    "Moisture": 33.5,
    "Soil Type": 1,
    "Crop Type": 2,
    "Nitrogen": 22,
    "Potassium": 18,
    "Phosphorous": 20
}

