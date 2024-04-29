from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model('model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        input_data = request.form['input_data']

        # Preprocess the input data (similar to how you preprocessed your training data)
        # Make sure to handle any data conversions or preprocessing steps required by your model

        # Perform prediction using the loaded model
        prediction = model.predict(np.array([input_data]))

        # Process the prediction results and format them as needed for display

        # Return the prediction result or render a new template with the result
        return render_template('IRT.html', prediction=prediction)
