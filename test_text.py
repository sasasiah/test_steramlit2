import streamlit as st
from transformers import pipeline

# Set a title and a subtitle
st.title("Sentiment Analysis App")
st.subheader("Analyze the sentiment of your text")

# Create a text input field for user input
user_input = st.text_area("Enter text here:")

# Check if user has entered any text
if user_input:
    # Load the sentiment analysis model
    sentiment_analyzer = pipeline("sentiment-analysis")

    # Analyze the sentiment of the user's text
    result = sentiment_analyzer(user_input)

    # Display the sentiment analysis result
    sentiment = result[0]['label']
    confidence = result[0]['score']
    st.write(f"Sentiment: {sentiment} (Confidence: {confidence:.2f})")

if user_input:
    # Load the text summarization model
    summarizer = pipeline("summarization")

    # Summarize the user's text
    summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)

    # Display the summary
    st.write("Summary:")
    st.write(summary[0]["summary_text"])