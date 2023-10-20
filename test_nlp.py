import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the lemmatizer and sentiment analyzer
lemmatizer = WordNetLemmatizer()
sentiment_analyzer = SentimentIntensityAnalyzer()

# Define the preprocessing function
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords and punctuation
    tokens = [token.lower() for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

# Define the sentiment analysis function
def analyze_sentiment(text):
    # Preprocess text
    tokens = preprocess_text(text)

    # Analyze sentiment
    sentiment_score = sentiment_analyzer.polarity_scores(text)

    return sentiment_score

# Create a Streamlit app
st.title("NLP App")

text = st.text_input("Enter your text here:")

if text:
    sentiment_score = analyze_sentiment(text)
    st.write(f"Sentiment Score: {sentiment_score}")
