import streamlit as st
import pandas as pd
#import plotly.express as px
#from transformers import pipeline
# Set a title for your Streamlit app
st.title("Animated 2D Line Chart from CSV")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Display the data
    st.subheader("Data Preview:")
    st.write(data)

    # Create an animated 2D line chart using Plotly
    st.subheader("Animated Line Chart")

    x_column = st.selectbox("Select X-axis data", options=data.columns)
    y_column = st.selectbox("Select Y-axis data", options=data.columns)
    animation_column = st.selectbox("Select Animation data", options=data.columns)

    animated_line_chart = px.line(data, x=x_column, y=y_column, animation_frame=animation_column,
                                  title="Animated 2D Line Chart")
    st.plotly_chart(animated_line_chart)

# You can add more features and components to your Streamlit app here
