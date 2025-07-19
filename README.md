# AI Salary Predictor

This is a Streamlit web application that predicts an individual's estimated salary based on input features such as age,gender,education level,job title, and years of experience. The app uses a Linear Regression model trained on structured salary data.

## Features

- Predict salary in real-time based on user input
- Machine Learning model built using `scikit-learn`
- Beautiful Streamlit UI 
- Input encoding and preprocessing handled dynamically
- Trained model saved and reused using `pickle`

## App Preview

![App Screenshot](screenshot.png)

## Installation Guide

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Streamlit

### Run Locally

#### 1. Clone the repository

```bash
git clone https://github.com/AditiSingh009/salary-prediction-app.git
cd salary-prediction-app

#### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows

#### 3. Install required packages

```bash
pip install -r requirements.txt

#### 4. Run the Streamlit app

```bash
streamlit run app.py

## Technologies Used

- Python

- Pandas

- Scikit-learn

- Streamlit

- Pickle




