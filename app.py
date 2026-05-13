import streamlit as st
import pandas as pd
import joblib

st.title("Penguin Body Mass Predictor")

# Load the model
model = joblib.load('penguin_model.joblib')

st.sidebar.header('User Input Features')

def user_input_features():
    island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    # Added the missing species column here
    species = st.sidebar.selectbox('Species', ('Adelie', 'Chinstrap', 'Gentoo'))
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    
    data = {'species': species,
            'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'sex': sex}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input parameters')
st.write(input_df)

# Prediction
try:
    prediction = model.predict(input_df)
    st.subheader('Prediction')
    st.write(f"The predicted body mass is **{prediction[0]:.2f} grams**")
except Exception as e:
    st.error(f"Prediction failed: {e}")
