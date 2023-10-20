import streamlit as st
import pandas as pd
import plotly.express as px

# Set a title and a subtitle
st.title("Interactive Dataset Dashboard")
st.subheader("Explore and Visualize Data")

# Create a file uploader to allow users to upload a dataset
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Load the dataset into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Display the raw data
    st.subheader("Raw Data")
    st.write(data)

    # Create a sidebar for data filtering
    st.sidebar.subheader("Data Filtering")

    # Allow the user to select columns for visualization
    columns = st.sidebar.multiselect("Select Columns for Visualization", data.columns)

    # Filter data based on user selection
    if columns:
        filtered_data = data[columns]
        st.subheader("Filtered Data")
        st.write(filtered_data)

        # Create scatter plot for filtered data
        st.subheader("Scatter Plot")
        fig = px.scatter(filtered_data, x=columns[0], y=columns[1])
        st.plotly_chart(fig)

# Provide instructions for the user
st.sidebar.markdown("To use this app, please upload a CSV file and select columns for visualization in the sidebar.")
