import streamlit as st
import pickle

# Load trained model and TF-IDF vectorizer
model = pickle.load(open("trained_model.sav", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.sav", "rb"))

st.title("📧 Spam Mail Classifier")

# Input text from user
input_mail = st.text_area("Enter your email/message text:")

if st.button("Predict"):
    if input_mail.strip() == "":
        st.warning("Please enter some text to classify!")
    else:
        # Convert input text to feature vectors
        input_features = vectorizer.transform([input_mail])
        # Make prediction
        prediction = model.predict(input_features)
        
        if prediction[0] == 0:
            st.error("This is a SPAM mail!")
        else:
            st.success("This is a HAM (not spam) mail!")
