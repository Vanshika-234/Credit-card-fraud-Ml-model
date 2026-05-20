import streamlit as st
import joblib

# Load model
model = joblib.load(
    r"C:\Users\vansh\Downloads\credit_card_fraud_model.pkl"
)

st.title("Credit Card Fraud Detection")

features = []

for i in range(30):
    value = st.number_input(f"Feature {i+1}")
    features.append(value)

if st.button("Predict"):

    prediction = model.predict([features])

    if prediction[0] == 0:
        st.success("Normal Transaction")
    else:
        st.error("Fraud Detected")