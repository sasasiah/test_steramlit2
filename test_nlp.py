import streamlit as st
import spacy

# Check if the spaCy model is already installed, and if not, download it.
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.warning("Downloading spaCy model. This may take a while.")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Set a title and a subtitle
st.title("NLP Text Analysis")
st.subheader("Analyze text with spaCy")

# Create a textarea for user input
text = st.text_area("Enter text for analysis", "")

# Analyze the text using spaCy
if text:
    doc = nlp(text)

    # Display the tokenized text
    st.subheader("Tokenized Text")
    for token in doc:
        st.write(token.text)

    # Display named entities
    st.subheader("Named Entities")
    for ent in doc.ents:
        st.write(f"{ent.text} ({ent.label_})")

    # Display parts of speech
    st.subheader("Parts of Speech")
    for token in doc:
        st.write(f"{token.text} - {token.pos_}")

    # Display dependencies
    st.subheader("Syntactic Dependencies")
    for token in doc:
        st.write(f"{token.text} - {token.dep_}")

    # Sentiment Analysis using TextBlob
    sentiment = TextBlob(text)
    sentiment_score = sentiment.sentiment.polarity
    st.subheader("Sentiment Analysis")

    # Display the sentiment score
    st.write(f"Sentiment Score: {sentiment_score}")

    # Categorize the sentiment
    if sentiment_score > 0:
        st.write("Sentiment: Positive")
    elif sentiment_score < 0:
        st.write("Sentiment: Negative")
    else:
        st.write("Sentiment: Neutral")
