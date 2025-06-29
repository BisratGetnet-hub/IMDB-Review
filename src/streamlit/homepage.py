import streamlit as st
import joblib
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from utils import clean_text

st.header("Python AI Developer Mini Project | By: Bisrat Getnet")
st.divider()


with st.form("sentiment_form"):
    review = st.text_area("Enter your movie review:", height=100)
    submit = st.form_submit_button("Predict Sentiment")

if submit:
    if review.strip() == "":
        st.warning("⚠️ Please enter a review before submitting.")
    else:
        pipeline = joblib.load("../../Model/logistic_model.pkl")
        text = clean_text(review)
        prediction = pipeline.predict([text])[0]
        if prediction == 1:
            st.success(f"🧠 Predicted Sentiment: **Positive**")
        else:
            st.error(f"🧠 Predicted Sentiment: **Negative**")