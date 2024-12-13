import streamlit as st
import json
import pickle
from streamlit_lottie import st_lottie
import numpy as np

# Sidebar with Title
st.sidebar.markdown("<h1 style='text-align: center; font-size: 3em; color: white;'>HEART DISEASE PREDICTION</h1>", unsafe_allow_html=True)

# Function to load Lottie animation from a local file
def load_lottie_file(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

# Load the trained model
with open('heart_disease_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load Lottie animation from local file
lottie_animation = load_lottie_file("lottie_img.json")

# Custom CSS to adjust sidebar width, background color, and center Lottie animation
st.markdown(
    """
    <style>
        /* Center the Lottie animation */
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Center the Lottie animation inside the sidebar
with st.sidebar:
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st_lottie(lottie_animation, speed=1, width=500, height=500, key="lottie")
    st.markdown('</div>', unsafe_allow_html=True)


# Main form
# st.title("Please enter the following details:")

with st.form(key='heart_disease_form', clear_on_submit=False):
    # Create two columns for side-by-side input fields
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, value=30, step=1)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, value=0, step=1)
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=200, value=120, step=1)
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=100, max_value=600, value=200, step=1)
        restecg = st.number_input('Resting Electrocardiographic Results (0-2)', min_value=0, max_value=2, value=0, step=1)
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=250, value=150, step=1)

    with col2:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['No', 'Yes'])
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
        slope = st.number_input('Slope of Peak Exercise ST Segment (0-2)', min_value=0, max_value=2, value=1, step=1)
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy (0-4)', min_value=0, max_value=4, value=0, step=1)
        thal = st.number_input('Thalassemia (1-3)', min_value=1, max_value=3, value=2, step=1)

    # Prepare input features for prediction
    sex_encoded = 1 if sex == 'Male' else 0
    fbs_encoded = 1 if fbs == 'Yes' else 0
    exang_encoded = 1 if exang == 'Yes' else 0

    user_input = np.array([[
        age, sex_encoded, cp, trestbps, chol, fbs_encoded,
        restecg, thalach, exang_encoded, oldpeak, slope, ca, thal
    ]])

    # Centered prediction button
    predict_button = st.form_submit_button('Predict Heart Disease Risk', use_container_width=True)

# Trigger the prediction only after the button is pressed
if predict_button:
    prediction = model.predict(user_input)

    # Display the prediction result with custom styling
    if prediction == 1:
        st.markdown('<div class="result">Result: The person is at risk of heart disease. Please consult a healthcare professional for further assessment.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result">**Result: The person is not at risk of heart disease based on the given data.</div>', unsafe_allow_html=True)

# Add custom CSS to center the button
st.markdown(
    """
    <style>
        .stButton > button {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    """, unsafe_allow_html=True
)
