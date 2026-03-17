import streamlit as st
import joblib

# Load
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
labels = joblib.load("labels.pkl")

st.title("Emotion Detection App")

text = st.text_input("Enter text")

if st.button("Predict"):
    if text.strip():
        vec = vectorizer.transform([text])

        pred = model.predict(vec)[0]
        probs = model.predict_proba(vec)[0]

        # Main prediction
        st.success(f"Predicted Emotion: {labels[pred]}")

        # Show probabilities
        st.subheader("Confidence Scores")
        for i, p in enumerate(probs):
            st.write(f"{labels[i]} : {round(p, 3)}")

    else:
        st.warning("Enter valid text")