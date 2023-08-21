from flask import Flask, request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('deployment_lin')
cols = ['town', 'flat_type', 'storey_range', 'floor_area_sqm', 'lease_commence_date', 'cbd_dist', 'min_dist_mrt']

@app.route('/')
def home():
    return render_template("hdbhome.html")

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns=cols)
    prediction = predict_model(model, data=data_unseen, round=0)
    
    predicted_value_column = prediction.columns[-1]  
    predicted_value = int(prediction[predicted_value_column][0])
    
    return render_template('hdbhome.html', pred='Expected Bill will be {}'.format(predicted_value))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    
    predicted_value_column = prediction.columns[-1]  
    predicted_value = prediction[predicted_value_column][0]
    
    return jsonify(predicted_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
