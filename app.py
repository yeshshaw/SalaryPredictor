# app.py code in Jupyter cell
from flask import Flask, request, jsonify
import pickle
import numpy as np
import os  # <- Add this

# Flask app
app = Flask(__name__)

# Load trained ML model
with open('linear_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Prediction route
@app.route('/predict', methods=['GET'])
def predict():
    # Get age from query parameter
    age = float(request.args.get('age'))
    # Predict salary
    salary = model.predict(np.array([[age]]))[0]
    # Return as JSON
    return jsonify({'salary': float(salary)})

# Run Flask server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # <- Use Render PORT
    app.run(host='0.0.0.0', port=port, debug=True)  # <- Bind to 0.0.0.0