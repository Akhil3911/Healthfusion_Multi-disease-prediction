import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
breast_cancer_model = pickle.load(open(f'{working_dir}/saved_models/breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'gender-female'],
                           default_index=0)

# =========================
# Diabetes Prediction Page
# =========================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies [0–20]",
                                      min_value=0, max_value=20, value=1,
                                      help="Number of times pregnant.")

    with col2:
        Glucose = st.number_input("Glucose Level (mg/dL) [50–250]",
                                  min_value=50, max_value=250, value=120,
                                  help="Normal fasting range: 70–100 mg/dL. Above 140 may indicate diabetes.")

    with col3:
        BloodPressure = st.number_input("Blood Pressure (mm Hg) [40–200]",
                                        min_value=40, max_value=200, value=80,
                                        help="Typical healthy range: 80–120 mm Hg.")

    with col1:
        SkinThickness = st.number_input("Skin Thickness (mm) [0–100]",
                                        min_value=0, max_value=100, value=20,
                                        help="Skin fold thickness measurement in mm.")

    with col2:
        Insulin = st.number_input("Insulin Level (µU/mL) [0–900]",
                                  min_value=0, max_value=900, value=85,
                                  help="Normal fasting insulin: 2–25 µU/mL.")

    with col3:
        BMI = st.number_input("BMI value [10–60]",
                              min_value=10.0, max_value=60.0, value=25.0,
                              help="Body Mass Index = weight(kg)/height(m²). Normal range: 18.5–24.9.")

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function [0.0–2.5]",
                                                   min_value=0.0, max_value=2.5, value=0.5,
                                                   help="A function which scores likelihood of diabetes based on family history.")

    with col2:
        Age = st.number_input("Age of the Person [1–120]",
                              min_value=1, max_value=120, value=30,
                              help="Age in years.")

    # Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness,
                      Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# =========================
# Heart Disease Prediction Page
# =========================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age [1–120]", min_value=1, max_value=120, value=40,
                              help="Age of the patient in years.")

    with col2:
        sex = st.number_input("Sex [0–1]", min_value=0, max_value=1, value=1,
                              help="0 = Female, 1 = Male.")

    with col3:
        cp = st.number_input("Chest Pain Type [0–3]", min_value=0, max_value=3, value=0,
                             help="0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic.")

    with col1:
        trestbps = st.number_input("Resting Blood Pressure (mm Hg) [80–200]",
                                   min_value=80, max_value=200, value=120,
                                   help="Resting blood pressure in mm Hg.")

    with col2:
        chol = st.number_input("Cholesterol (mg/dL) [100–600]",
                               min_value=100, max_value=600, value=200,
                               help="Serum cholesterol level.")

    with col3:
        fbs = st.number_input("Fasting Blood Sugar [0–1]",
                              min_value=0, max_value=1, value=0,
                              help="1 = FBS > 120 mg/dL, 0 = otherwise.")

    with col1:
        restecg = st.number_input("Resting ECG [0–2]", min_value=0, max_value=2, value=1,
                                  help="0: Normal, 1: ST-T abnormality, 2: Left ventricular hypertrophy.")

    with col2:
        thalach = st.number_input("Max Heart Rate [60–220]", min_value=60, max_value=220, value=150,
                                  help="Maximum heart rate achieved.")

    with col3:
        exang = st.number_input("Exercise Induced Angina [0–1]", min_value=0, max_value=1, value=0,
                                help="1 = Yes, 0 = No.")

    with col1:
        oldpeak = st.number_input("ST Depression [0.0–6.0]", min_value=0.0, max_value=6.0, value=1.0,
                                  help="ST depression induced by exercise relative to rest.")

    with col2:
        slope = st.number_input("Slope of ST Segment [0–2]", min_value=0, max_value=2, value=1,
                                help="0: Upsloping, 1: Flat, 2: Downsloping.")

    with col3:
        ca = st.number_input("Major Vessels (0–4)", min_value=0, max_value=4, value=0,
                             help="Number of major vessels colored by fluoroscopy.")

    with col1:
        thal = st.number_input("Thalassemia [0–2]", min_value=0, max_value=2, value=1,
                               help="0 = Normal, 1 = Fixed defect, 2 = Reversible defect.")

    # Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca, thal]
        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# =========================
# Parkinson's Prediction Page
# =========================
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz) [80–300]", min_value=80.0, max_value=300.0, value=120.0,
                             help="Average vocal fundamental frequency.")

    with col2:
        fhi = st.number_input("MDVP:Fhi(Hz) [100–600]", min_value=100.0, max_value=600.0, value=200.0,
                              help="Maximum vocal fundamental frequency.")

    with col3:
        flo = st.number_input("MDVP:Flo(Hz) [50–200]", min_value=50.0, max_value=200.0, value=90.0,
                              help="Minimum vocal fundamental frequency.")

    with col4:
        Jitter_percent = st.number_input("MDVP:Jitter(%) [0–1]", min_value=0.0, max_value=1.0, value=0.01,
                                         help="Measure of variation in fundamental frequency.")

    with col5:
        Jitter_Abs = st.number_input("MDVP:Jitter(Abs) [0–1]", min_value=0.0, max_value=1.0, value=0.005,
                                     help="Absolute jitter value.")

    with col1:
        RAP = st.number_input("MDVP:RAP [0–1]", min_value=0.0, max_value=1.0, value=0.01,
                              help="Relative average perturbation.")

    with col2:
        PPQ = st.number_input("MDVP:PPQ [0–1]", min_value=0.0, max_value=1.0, value=0.01,
                              help="Pitch period perturbation quotient.")

    with col3:
        DDP = st.number_input("Jitter:DDP [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                              help="Difference of differences of periods.")

    with col4:
        Shimmer = st.number_input("MDVP:Shimmer [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                                  help="Variation in amplitude.")

    with col5:
        Shimmer_dB = st.number_input("MDVP:Shimmer(dB) [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                                     help="Shimmer in decibels.")

    with col1:
        APQ3 = st.number_input("Shimmer:APQ3 [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                               help="Amplitude perturbation quotient (3 cycles).")

    with col2:
        APQ5 = st.number_input("Shimmer:APQ5 [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                               help="Amplitude perturbation quotient (5 cycles).")

    with col3:
        APQ = st.number_input("MDVP:APQ [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                              help="Amplitude perturbation quotient.")

    with col4:
        DDA = st.number_input("Shimmer:DDA [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                              help="Difference of differences of amplitude.")

    with col5:
        NHR = st.number_input("NHR [0–1]", min_value=0.0, max_value=1.0, value=0.02,
                              help="Noise-to-harmonics ratio.")

    with col1:
        HNR = st.number_input("HNR [0–100]", min_value=0.0, max_value=100.0, value=20.0,
                              help="Harmonics-to-noise ratio.")

    with col2:
        RPDE = st.number_input("RPDE [0–1]", min_value=0.0, max_value=1.0, value=0.5,
                               help="Recurrence period density entropy.")

    with col3:
        DFA = st.number_input("DFA [0–1]", min_value=0.0, max_value=1.0, value=0.5,
                              help="Signal fractal scaling exponent.")

    with col4:
        spread1 = st.number_input("Spread1 [–1–1]", min_value=-1.0, max_value=1.0, value=0.0,
                                  help="Nonlinear measure of fundamental frequency variation.")

    with col5:
        spread2 = st.number_input("Spread2 [–1–1]", min_value=-1.0, max_value=1.0, value=0.0,
                                  help="Nonlinear measure of fundamental frequency variation.")

    with col1:
        D2 = st.number_input("D2 [0–3]", min_value=0.0, max_value=3.0, value=1.0,
                             help="Correlation dimension.")

    with col2:
        PPE = st.number_input("PPE [0–1]", min_value=0.0, max_value=1.0, value=0.5,
                              help="Pitch period entropy.")

    # Prediction
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                      APQ3, APQ5, APQ, DDA, NHR, HNR,
                      RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


# =========================
# Breast Cancer Prediction Page (Fixed)
# =========================
if selected == "Breast Cancer Prediction":
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.number_input("Mean Radius [5–30]", min_value=5.0, max_value=30.0, value=14.0,
                                      help="Mean of distances from center to points on the perimeter.")

    with col2:
        mean_texture = st.number_input("Mean Texture [5–40]", min_value=5.0, max_value=40.0, value=20.0,
                                       help="Standard deviation of gray-scale values.")

    with col3:
        mean_perimeter = st.number_input("Mean Perimeter [40–200]", min_value=40.0, max_value=200.0, value=90.0,
                                         help="Mean size of perimeter across cells.")

    with col1:
        mean_area = st.number_input("Mean Area [100–2500]", min_value=100.0, max_value=2500.0, value=700.0,
                                    help="Mean area of the cells.")

    with col2:
        mean_smoothness = st.number_input("Mean Smoothness [0.05–0.2]", min_value=0.05, max_value=0.2, value=0.1,
                                          help="Mean smoothness of cell nuclei.")

    # --- Load feature list dynamically ---
    features_path = os.path.join(working_dir, "saved_models", "breast_cancer_features.sav")
    if os.path.exists(features_path):
        feature_list = pickle.load(open(features_path, "rb"))
    else:
        feature_list = ['mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area', 'mean_smoothness']

    input_values = {
        'mean_radius': mean_radius,
        'mean_texture': mean_texture,
        'mean_perimeter': mean_perimeter,
        'mean_area': mean_area,
        'mean_smoothness': mean_smoothness
    }

    user_input = [input_values.get(f, 0) for f in feature_list]

    # Prediction
    breast_diagnosis = ''
    if st.button("Breast Cancer Test Result"):
        breast_prediction = breast_cancer_model.predict([user_input])

        if breast_prediction[0] == 1:
            breast_diagnosis = "⚠️ The tumor is Malignant (Cancerous)"
        else:
            breast_diagnosis = "✅ The tumor is Benign (Not Cancerous)"

    st.success(breast_diagnosis)
