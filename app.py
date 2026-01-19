from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import os
import traceback

app = Flask(__name__)
CORS(app)

# Load model dan scaler
try:
    model_path = os.path.join(os.path.dirname(__file__), 'model', 'trained_logreg_model.pkl')
    scaler_path = os.path.join(os.path.dirname(__file__), 'model', 'scaler.pkl')
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    
    print("✓ Model dan scaler berhasil dimuat")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    model = None
    scaler = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Validasi input
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Ambil 4 features dari request (x1, x2, x3, x4)
        features = []
        for key in ['x1', 'x2', 'x3', 'x4']:
            if key in data:
                try:
                    features.append(float(data[key]))
                except ValueError:
                    return jsonify({'error': f'Invalid value for {key}'}), 400
            else:
                return jsonify({'error': f'Missing feature: {key}'}), 400
        
        # Scale features
        features_array = np.array([features])
        features_scaled = scaler.transform(features_array)
        
        # Predict
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        confidence = float(max(probability)) * 100
        
        return jsonify({
            'prediction': float(prediction),
            'probability': [float(p) for p in probability],
            'confidence': confidence
        })
    
    except Exception as e:
        print(f"Error in predict: {e}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'model_loaded': model is not None,
        'scaler_loaded': scaler is not None
    })

if __name__ == '__main__':
    app.run(debug=False)
