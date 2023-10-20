import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
# Set a title for your Streamlit app
st.title("Random Number Generator")

# Create a button that generates and displays a random number when clicked
if st.button("Generate Random Number"):
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    st.write(f"Random Number: {random_number}")

# Set a title for your Streamlit app
st.title("CSV File Uploader and Summary")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Display the data
    st.subheader("Data Preview:")
    st.write(data)

    # Visualize the data as a line plot
    st.subheader("Line Plot")
    x_column = st.selectbox("Select X-axis data", options=data.columns)
    y_column = st.selectbox("Select Y-axis data", options=data.columns)
    color_column = st.selectbox("Select Color data", options=data.columns)

    scatter_plot = px.scatter(data, x=x_column, y=y_column, color=color_column)
    st.plotly_chart(scatter_plot)

    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        ax.plot(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

