import streamlit as st
import pandas as pd
import pickle

# Page settings
st.set_page_config(page_title="AI Salary Predictor", page_icon="💰", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0e1117;
        color: #ffffff;
    }

    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }

    .title {
        font-size: 3em;
        font-weight: bold;
        color: #00FFAA;
        text-align: center;
    }

    .subtitle {
        font-size: 1.2em;
        color: #AAAAAA;
        text-align: center;
        margin-bottom: 20px;
    }

    .salary-box {
        font-size: 2em;
        font-weight: bold;
        color: #00FFAA;
        background-color: #1f2937;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
    }

    /* Fix label text */
    label, .css-1cpxqw2 {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* Fix dropdown input text */
    .css-1d391kg > div > div {
        color: white !important;
        background-color: #1f2937 !important;
    }

    /* Fix dropdown popup options */
    .css-11unzgr {
        background-color: #1f2937 !important;
        color: white !important;
    }

    /* Fix the text input boxes */
    .stTextInput > div > div > input {
        color: white;
        background-color: #1f2937;
    }

    </style>
""", unsafe_allow_html=True)




# Title
st.markdown("<div class='title'>💼 AI Salary Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Predict salary based on your profile</div>", unsafe_allow_html=True)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Form
with st.form("salary_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("👤 Age", min_value=18, max_value=65, value=25)
        gender = st.selectbox("⚧ Gender", ["Male", "Female"])
        education = st.selectbox("🎓 Education Level", ["High School", "Bachelor's", "Master's", "PhD"])

    with col2:
        job_title = st.selectbox("💼 Job Title", [
            "Software Engineer", "Data Scientist", "Product Manager",
            "Designer", "Accountant", "Administrative Assistant"
        ])
        experience = st.number_input("📈 Years of Experience", min_value=0.0, max_value=50.0, value=1.0)

    submitted = st.form_submit_button("🚀 Predict Salary")

# Prediction
if submitted:
    input_df = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education],
        'Job Title': [job_title],
        'Years of Experience': [experience]
    })

    prediction = model.predict(input_df)[0]

    st.markdown(f"<div class='salary-box'>Predicted Salary: ₹{prediction:,.2f}</div>", unsafe_allow_html=True)
