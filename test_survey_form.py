import streamlit as st

# Set a title and a subtitle
st.title("Survey Form App")
st.subheader("Create an interactive survey form")

# Create a sidebar with user input for survey questions
number_of_questions = st.sidebar.number_input("Number of Questions", min_value=1, max_value=10, value=3)
questions = []
for i in range(number_of_questions):
    question = st.sidebar.text_input(f"Question {i + 1}")
    questions.append(question)

# Create a form to collect survey responses
st.subheader("Survey Form")
responses = []
for i, question in enumerate(questions):
    response = st.text_input(f"Response to Question {i + 1}", key=f"response_{i}")
    responses.append(response)

# Display responses
st.subheader("Survey Responses")
for i, response in enumerate(responses):
    st.write(f"Question {i + 1}: {questions[i]}")
    st.write(f"Response: {response}")

# Submit button to save responses
if st.button("Submit Survey"):
    st.write("Survey responses submitted successfully.")
