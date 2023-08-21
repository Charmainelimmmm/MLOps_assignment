from flask import Flask, request, render_template, jsonify
from pycaret.anomaly import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model and other necessary objects here
# For this example, let's load a pre-trained Isolation Forest model
model = load_model('Final IForest Model')
cols = ['TRANS_DT', 'AMT', 'FISCAL_YR', 'FISCAL_MTH']

# Define a route to serve the HTML form
@app.route('/anomalydetection')
def index():
    return render_template('home3.html')

# Define a route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns=cols)
    prediction = predict_model(model, data=data_unseen)
    
    # Anomaly column name might vary based on your model or preprocessing
    anomaly_column = 'Anomaly'
    
    prediction_anomaly = int(round(prediction[anomaly_column][0]))
    return render_template('home3.html', pred='Anomaly Detected {}'.format(prediction_anomaly))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    predictions = predict_model(model, data=data_unseen)
    
    # Anomaly column name might vary based on your model or preprocessing
    anomaly_column = 'Anomaly'
    
    output = int(round(predictions[anomaly_column][0]))
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)


