from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model_path = os.path.join("Models", "rf_classifier.pkl")
scaler_path = os.path.join("Models", "scaler.pkl")

model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))


# Prediction logic
def predict(model, scaler, male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes,
            totChol, sysBP, diaBP, BMI, heartRate, glucose):
    male_encoded = 1 if male.lower() == "male" else 0
    currentSmoker_encoded = 1 if currentSmoker.lower() == "yes" else 0
    BPMeds_encoded = 1 if BPMeds.lower() == "yes" else 0
    prevalentStroke_encoded = 1 if prevalentStroke.lower() == "yes" else 0
    prevalentHyp_encoded = 1 if prevalentHyp.lower() == "yes" else 0
    diabetes_encoded = 1 if diabetes.lower() == "yes" else 0

    features = np.array([[male_encoded, age, currentSmoker_encoded, cigsPerDay,
                          BPMeds_encoded, prevalentStroke_encoded, prevalentHyp_encoded, diabetes_encoded,
                          totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    scaled_features = scaler.transform(features)
    result = model.predict(scaled_features)

    return result[0]


# Routes
@app.route('/Home1.html')
def home():
    return render_template('Home1.html')
@app.route('/Index1.html')
def index1():
    return render_template('Index1.html')
@app.route('/index.html')
def index():
    return render_template('Home1.html')


@app.route('/Symptoms.html')
def symptoms():
    return render_template('Symptoms.html')

@app.route('/Contacts.html')
def contacts():
    return render_template('Contacts.html')

@app.route('/')
def redirect_to_home():
    return render_template('Home1.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        # Get form data
        male = request.form['male']
        age = int(request.form['age'])
        currentSmoker = request.form['currentSmoker']
        cigsPerDay = float(request.form['cigsPerDay'])
        BPMeds = request.form['BPMeds']
        prevalentStroke = request.form['prevalentStroke']
        prevalentHyp = request.form['prevalentHyp']
        diabetes = request.form['diabetes']
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])

        # Predict
        prediction = predict(model, scaler, male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke,
                             prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose)

        prediction_text = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"

        return render_template('predict.html', prediction=prediction_text)

    except Exception as e:
        return render_template('predict.html', prediction=f"Error in input: {str(e)}")



if __name__ == '__main__':
    app.run(debug=True)

