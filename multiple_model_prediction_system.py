import streamlit as st
import pickle
from streamlit_option_menu import option_menu


# ---------------------------------------------------
# Loading the trained models
# ---------------------------------------------------

diabetes_model = pickle.load(open("trained_model.sav", "rb"))
heart_disease_model = pickle.load(open("heart_diseases.sav", "rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))


# ---------------------------------------------------
# Sidebar menu
# ---------------------------------------------------

with st.sidebar:

    selected = option_menu(
        "Multiple Disease Prediction System",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinsons Prediction"
        ],
        icons=[
            "activity",
            "heart",
            "person"
        ],
        default_index=0
    )


# ===================================================
# Diabetes Prediction
# ===================================================

if selected == "Diabetes Prediction":

    st.title("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure")

    with col1:
        SkinThickness = st.text_input("Skin Thickness")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI")

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            "Diabetes Pedigree Function"
        )

    with col2:
        Age = st.text_input("Age")

    diabetes_diagnosis = ""

    if st.button("Diabetes Test Result"):

        try:

            diabetes_prediction = diabetes_model.predict([[
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]])

            if diabetes_prediction[0] == 1:
                diabetes_diagnosis = "The person is diabetic"
            else:
                diabetes_diagnosis = "The person is not diabetic"

        except ValueError:
            diabetes_diagnosis = "Please enter valid numerical values."

    st.success(diabetes_diagnosis)


# ===================================================
# Heart Disease Prediction
# ===================================================

if selected == "Heart Disease Prediction":

    st.title("Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")

    with col2:
        sex = st.text_input("Sex")

    with col3:
        cp = st.text_input("Chest Pain Type")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")

    with col2:
        chol = st.text_input("Cholesterol")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar")

    with col1:
        restecg = st.text_input("Resting ECG")

    with col2:
        thalach = st.text_input("Maximum Heart Rate")

    with col3:
        exang = st.text_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.text_input("ST Depression")

    with col2:
        slope = st.text_input("Slope")

    with col3:
        ca = st.text_input("Number of Major Vessels")

    with col1:
        thal = st.text_input("Thalassemia")

    heart_diagnosis = ""

    if st.button("Heart Disease Test Result"):

        try:

            heart_prediction = heart_disease_model.predict([[
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]])

            if heart_prediction[0] == 1:
                heart_diagnosis = "The person has heart disease"
            else:
                heart_diagnosis = "The person does not have heart disease"

        except ValueError:
            heart_diagnosis = "Please enter valid numerical values."

    st.success(heart_diagnosis)


# ===================================================
# Parkinson's Disease Prediction
# ===================================================

if selected == "Parkinsons Prediction":

    st.title("Parkinson's Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")

    with col1:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col2:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")

    with col3:
        RAP = st.text_input("MDVP:RAP")

    with col1:
        PPQ = st.text_input("MDVP:PPQ")

    with col2:
        DDP = st.text_input("Jitter:DDP")

    with col3:
        Shimmer = st.text_input("MDVP:Shimmer")

    with col1:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")

    with col2:
        APQ3 = st.text_input("Shimmer:APQ3")

    with col3:
        APQ5 = st.text_input("Shimmer:APQ5")

    with col1:
        APQ = st.text_input("MDVP:APQ")

    with col2:
        DDA = st.text_input("Shimmer:DDA")

    with col3:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")

    with col2:
        RPDE = st.text_input("RPDE")

    with col3:
        DFA = st.text_input("DFA")

    with col1:
        spread1 = st.text_input("spread1")

    with col2:
        spread2 = st.text_input("spread2")

    with col3:
        D2 = st.text_input("D2")

    with col1:
        PPE = st.text_input("PPE")

    parkinsons_diagnosis = ""

    if st.button("Parkinson's Test Result"):

        try:

            parkinsons_prediction = parkinsons_model.predict([[
                float(fo),
                float(fhi),
                float(flo),
                float(Jitter_percent),
                float(Jitter_Abs),
                float(RAP),
                float(PPQ),
                float(DDP),
                float(Shimmer),
                float(Shimmer_dB),
                float(APQ3),
                float(APQ5),
                float(APQ),
                float(DDA),
                float(NHR),
                float(HNR),
                float(RPDE),
                float(DFA),
                float(spread1),
                float(spread2),
                float(D2),
                float(PPE)
            ]])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        except ValueError:
            parkinsons_diagnosis = "Please enter valid numerical values."

    st.success(parkinsons_diagnosis)
