from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from catboost import CatBoostClassifier
from pycaret.classification import load_model, predict_model

app = Flask(__name__, template_folder='templates')

# Load the PyCaret model
model = load_model('heart_disease_model')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_data = {
            'age': [int(request.form['age'])],
            'gender': [request.form['gender']],
            'chest_pain': [request.form['chest_pain']],
            'resting_BP': [int(request.form['resting_BP'])],
            'cholesterol': [int(request.form['cholesterol'])],
            'fasting_BS': [int(request.form['fasting_BS'])],
            'resting_ECG': [request.form['resting_ECG']],
            'max_HR': [int(request.form['max_HR'])],
            'exercise_angina': [request.form['exercise_angina']],
            'old_peak': [float(request.form['old_peak'])],
            'ST_slope': [request.form['ST_slope']]
        }
        input_df = pd.DataFrame(input_data)

        predictions = predict_model(model, data=input_df)
        result = predictions['prediction_label'][0]

        # return redirect(url_for('show_result', result=result))

    return render_template('cv_predictor.html', result=result)

@app.route('/result/<int:result>')
def show_result(result):
    return render_template('prediction_result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
