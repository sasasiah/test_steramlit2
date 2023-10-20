import streamlit as st
import spacy

# Load the spaCy English language model
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
