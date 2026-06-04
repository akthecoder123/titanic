import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open('notebooks/model.pkl', 'rb'))

st.title("Titanic Survival Predictor 🚢")

pclass = st.selectbox("Passenger Class", [1,2,3])
age = st.slider("Age", 1, 80, 25)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)

sex = st.selectbox("Sex", ["Male", "Female"])

# encoding
male = 1 if sex == "Male" else 0

# prediction button
if st.button("Predict"):

    features = np.array([[pclass, age, fare, male]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Passenger Survived 😎")
    else:
        st.error("Passenger Did Not Survive 💀")