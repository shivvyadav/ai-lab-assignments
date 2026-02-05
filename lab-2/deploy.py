import streamlit as st
import joblib

st.title('News Category prediction')

model = joblib.load('model.joblib')

text = st.text_area('Enter news')

if st.button('Predict'):
    prediction = model.predict([text])[0]
    st.success(f"Predicted news category: {prediction}")
