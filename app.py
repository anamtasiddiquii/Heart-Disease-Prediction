import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load Model
# -----------------------------
with open("best_svm_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("feature_names.pkl", "rb") as file:
    feature_names = pickle.load(file)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's details below and click Predict.")

# -----------------------------
# Inputs
# -----------------------------

age = st.number_input("Age", 20, 100, 45)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox(
    "Chest Pain Type",
    [
        "0 - Typical Angina",
        "1 - Atypical Angina",
        "2 - Non-anginal Pain",
        "3 - Asymptomatic"
    ]
)
cp = int(cp[0])

trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    80,
    220,
    120
)

chol = st.number_input(
    "Serum Cholesterol (mg/dl)",
    100,
    600,
    240
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    ["No", "Yes"]
)
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox(
    "Resting ECG",
    [
        "0 - Normal",
        "1 - ST-T abnormality",
        "2 - Left ventricular hypertrophy"
    ]
)
restecg = int(restecg[0])

thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    60,
    220,
    150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input(
    "Oldpeak",
    0.0,
    6.5,
    1.0
)

slope = st.selectbox(
    "Slope",
    [0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    [
        "0 - Normal",
        "1 - Fixed Defect",
        "2 - Reversible Defect",
        "3 - Unknown"
    ]
)
thal = int(thal[0])

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    # One-hot Encoding

    cp1 = 1 if cp == 1 else 0
    cp2 = 1 if cp == 2 else 0
    cp3 = 1 if cp == 3 else 0

    rest1 = 1 if restecg == 1 else 0
    rest2 = 1 if restecg == 2 else 0

    thal1 = 1 if thal == 1 else 0
    thal2 = 1 if thal == 2 else 0
    thal3 = 1 if thal == 3 else 0

    input_data = pd.DataFrame(
        [[
            age,
            sex,
            trestbps,
            chol,
            fbs,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            cp1,
            cp2,
            cp3,
            rest1,
            rest2,
            thal1,
            thal2,
            thal3
        ]],
        columns=feature_names
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error("❤️ High Risk of Heart Disease")
        st.write(f"Confidence: **{probability[1]*100:.2f}%**")
    else:
        st.success("💚 Low Risk of Heart Disease")
        st.write(f"Confidence: **{probability[0]*100:.2f}%**")