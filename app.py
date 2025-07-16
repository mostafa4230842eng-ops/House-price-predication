import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('./Models/SDG.pkl')
# scaler = joblib.load('./Models/Scalar.pkl')

st.title("🏠 House Price Predictor (with Scaler)")

# User inputs
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 10, 2)
area = st.number_input("Area in square feet", min_value=100, value=1000)

# Collect inputs in same order as used during training
user_input = np.array([[bedrooms, bathrooms, area]])

# # Apply scaler
# scaled_input = scaler.transform(user_input)

if st.button("Predict"):
    prediction = model.predict(user_input)
    st.success(f"🏡 Estimated House Price: ${prediction:,.2f}")