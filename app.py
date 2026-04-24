import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("🏠 House Price Predictor")

X = np.array([[1000,2],[1500,3],[2000,3],[2500,4],[3000,5]])
y = np.array([30,50,65,80,100])

model = LinearRegression()
model.fit(X, y)

area = st.number_input("Enter Area", min_value=0)
bedrooms = st.number_input("Enter Bedrooms", min_value=0)

if st.button("Predict"):
    prediction = model.predict([[area, bedrooms]])
    st.success(f"Price: ₹ {prediction[0]:.2f} Lakhs")