import streamlit as st
import joblib
import numpy as np

import os

st.title("Student Performance Predictor")

# Find the directory containing this script and load model relative to it
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model file not found! Searched at: {model_path}")
    st.stop()

input1 = st.number_input("Enter Study Hours")
input2 = st.number_input("Enter Attendance")

if st.button("Predict"):
    prediction = model.predict([[input1, input2]])
    st.success(f"Predicted Score: {prediction[0]}")