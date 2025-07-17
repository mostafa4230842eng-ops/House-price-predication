import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load('./Models/SDG.pkl')
# scaler = joblib.load('./Models/Scalar.pkl')

st.title("🏠 House Price Predictor")

# إدخالات المستخدم
area = st.number_input("📏 Area (in sq ft)", min_value=100, value=1000)
bedrooms = st.slider("🛏️ Bedrooms", 1, 10, 3)
bathrooms = st.slider("🛁 Bathrooms", 1, 10, 2)
stories = st.slider("🏢 Stories", 1, 4, 2)

mainroad = st.selectbox("🚧 Access to Main Road", ['yes', 'no'])
guestroom = st.selectbox("🛋️ Guest Room", ['yes', 'no'])
basement = st.selectbox("🏗️ Basement", ['yes', 'no'])
hotwaterheating = st.selectbox("🔥 Hot Water Heating", ['yes', 'no'])
airconditioning = st.selectbox("❄️ Air Conditioning", ['yes', 'no'])
parking = st.slider("🚗 Parking Spaces", 0, 3, 1)
prefarea = st.selectbox("🌳 Preferred Area", ['yes', 'no'])
furnishingstatus = st.selectbox("🛋️ Furnishing Status", ['furnished', 'semi-furnished', 'unfurnished'])

# تجميع الإدخال في DataFrame بنفس ترتيب التدريب
user_input = pd.DataFrame([[
    area, bedrooms, bathrooms, stories,
    mainroad, guestroom, basement, hotwaterheating, airconditioning,
    parking, prefarea, furnishingstatus
]], columns=[
    'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
    'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
    'parking', 'prefarea', 'furnishingstatus'
])

# تحويل القيم النصية بنفس أسلوب التدريب
label_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
for col in label_cols:
    user_input[col] = user_input[col].map({'yes': 1, 'no': 0,
                                           'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0})

# إجراء التوقع
if st.button("🔍 Predict Price"):
    prediction = model.predict(user_input)[0]
    st.success(f"🏡 Estimated House Price: ₹ {prediction:,.0f}")
