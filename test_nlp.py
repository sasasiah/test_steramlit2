import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px

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
st.title("NLP Dashboard")

text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    # Word Segmentation
    st.subheader("Word Segmentation:")
    tokens = word_tokenize(text)
    st.write(tokens)

    # Sentiment Analysis
    sentiment_score = analyze_sentiment(text)
    st.subheader("Sentiment Analysis:")
    st.write(f"Sentiment Score: {sentiment_score['compound']}")

    # Visualization
    data = pd.DataFrame({'Sentiment': ['Positive', 'Negative', 'Neutral'], 'Count': [sentiment_score['pos'], sentiment_score['neg'], sentiment_score['neu']]})
    fig = px.bar(data, x='Sentiment', y='Count', color='Sentiment')
    st.plotly_chart(fig)

# Custom CSS styles
st.markdown(
    """
    <style>
    .stTextInput {background-color: #F4F4F4;}
    </style>
    """,
    unsafe_allow_html=True
)

# Custom background image
st.markdown(
    """
    <style>
    body {
    background-image: url('https://img.freepik.com/free-vector/background-realistic-abstract-technology-particle_23-2148431735.jpg?w=1380&t=st=1697787693~exp=1697788293~hmac=06a814fa711cf9cf3ab605f6333030fe3c670ecf0aedbb27424968b93daf1c9e');
    background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

