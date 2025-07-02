
from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Construct path to the model file relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, '..', '..', '5_modeling', 'model.pkl')
# Load the trained model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze')
def analyze():
    return render_template('visualization.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        form_data = request.form.to_dict()
        # Convert form data to a pandas DataFrame
        df = pd.DataFrame([form_data])
        # Make a prediction
        prediction = model.predict(df)[0]
        return render_template('predict.html', prediction=prediction)
    return render_template('predict.html', prediction=None)

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
