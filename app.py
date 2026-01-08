import streamlit as st
from inference.predictor import analyze

st.set_page_config(page_title="Cross-lingual Sentiment Analysis")

st.title("Cross-lingual Sentiment Analysis")

review = st.text_area("Enter an e-commerce review")

if st.button("Analyze Sentiment"):
    if review.strip():
        sentiment, confidence = analyze(review)

        if sentiment == "Positive":
            st.success(f"Sentiment: {sentiment} ({confidence})")
        elif sentiment == "Negative":
            st.error(f"Sentiment: {sentiment} ({confidence})")
        else:
            st.info(f"Sentiment: {sentiment} ({confidence})")
    else:
        st.warning("Please enter some text.")
