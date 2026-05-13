import streamlit as st
import pandas as pd
import joblib
import sklearn

st.title("Penguin Body Mass Predictor")

try:
    # Attempt to load the model
    model = joblib.load('penguin_model.joblib')
    st.success("Model loaded successfully!")
    
    # Insert your prediction logic here (sliders, inputs, etc.)
    
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.write("### Diagnostic Info:")
    st.write(f"**Current scikit-learn version:** {sklearn.__version__}")
    st.write(f"**Current Python version:** 3.12")
    st.info("If the version above doesn't match the one used to create the model, update your requirements.txt.")
