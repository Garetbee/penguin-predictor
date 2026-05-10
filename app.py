import streamlit as st
import pandas as pd
import joblib

# Load the model
# Ensure penguin_model.joblib is in the same folder as app.py
model = joblib.load('penguin_model.joblib')

st.title("🐧 Penguin Body Mass Predictor")
st.write("Enter the penguin's details below to predict its body mass in grams.")

# Layout with columns for better UI
col1, col2 = st.columns(2)

with col1:
    species = st.selectbox("Species", ["Adelie", "Chinstrap", "Gentoo"])
    island = st.selectbox("Island", ["Torgersen", "Biscoe", "Dream"])
    sex = st.selectbox("Sex", ["male", "female"])

with col2:
    bill_length = st.number_input("Bill Length (mm)", min_value=30.0, max_value=60.0, value=45.0)
    bill_depth = st.number_input("Bill Depth (mm)", min_value=13.0, max_value=22.0, value=17.0)
    flipper_length = st.number_input("Flipper Length (mm)", min_value=170, max_value=240, value=200)

# Create a dataframe for the model input
input_data = pd.DataFrame({
    'bill_length_mm': [bill_length],
    'bill_depth_mm': [bill_depth],
    'flipper_length_mm': [flipper_length],
    'species': [species],
    'island': [island],
    'sex': [sex]
})

if st.button("Predict Body Mass"):
    try:
        prediction = model.predict(input_data)
        st.success(f"The predicted body mass is: **{prediction[0]:.2f}g**")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

st.info("Note: This app uses a machine learning model trained on the Palmer Penguins dataset.")