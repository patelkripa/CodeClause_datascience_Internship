# heart_predictor.py

import streamlit as st
import joblib
import numpy as np

model = joblib.load("heart_model.pkl")

st.title("❤️ Heart Disease Risk Predictor")

# Input fields
age = st.number_input("Age", 20, 100)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox("Chest Pain Type", [
    "Typical Angina (0)",
    "Atypical Angina (1)",
    "Non-anginal Pain (2)",
    "Asymptomatic (3)"
])
cp = ["Typical Angina (0)", "Atypical Angina (1)", "Non-anginal Pain (2)", "Asymptomatic (3)"].index(cp)

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200)
chol = st.number_input("Cholesterol (mg/dl)", 100, 600)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Resting ECG Results", [
    "Normal (0)",
    "ST-T Wave Abnormality (1)",
    "Left Ventricular Hypertrophy (2)"
])
restecg = ["Normal (0)", "ST-T Wave Abnormality (1)", "Left Ventricular Hypertrophy (2)"].index(restecg)

thalach = st.number_input("Maximum Heart Rate Achieved", 60, 220)

exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.0, step=0.1)

slope = st.selectbox("Slope of Peak Exercise ST Segment", [
    "Upsloping (0)",
    "Flat (1)",
    "Downsloping (2)"
])
slope = ["Upsloping (0)", "Flat (1)", "Downsloping (2)"].index(slope)

ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (0–3)", [0, 1, 2, 3])

thal = st.selectbox("Thalassemia", [
    "Normal (1)",
    "Fixed Defect (2)",
    "Reversible Defect (3)"
])
thal = [1, 2, 3][["Normal (1)", "Fixed Defect (2)", "Reversible Defect (3)"].index(thal)]

# Prediction
if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease.")
    else:
        st.success("✅ Low risk of heart disease.")
