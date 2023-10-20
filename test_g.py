import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

# Set a title and a subtitle
st.title("Custom Chart App")
st.subheader("Create a custom chart with user-provided data")

# Create a sidebar with user input for chart type
chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter", "Line", "Bar", "Pie", "Box", "Area", "Histogram"])

# Create a file uploader for CSV files
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Allow users to select X and Y columns
    x_column = st.selectbox("Select X Column", df.columns)
    y_column = st.selectbox("Select Y Column", df.columns)

    # Allow users to select a column for color differentiation
    color_column = st.sidebar.selectbox("Select Color Column", df.columns)

    # Check for valid columns in the DataFrame
    if x_column != y_column:
        # Create a custom chart based on the selected chart type
        plt.figure(figsize=(10, 6))

        if chart_type == "Scatter":
            if color_column:
                sns.scatterplot(data=df, x=x_column, y=y_column, hue=color_column)
            else:
                sns.scatterplot(data=df, x=x_column, y=y_column)
            plt.title("Custom Scatter Plot")
        elif chart_type == "Line":
            if color_column:
                sns.lineplot(data=df, x=x_column, y=y_column, hue=color_column)
            else:
                sns.lineplot(data=df, x=x_column, y=y_column)
            plt.title("Custom Line Chart")
        elif chart_type == "Bar":
            if color_column:
                sns.barplot(data=df, x=x_column, y=y_column, hue=color_column)
            else:
                sns.barplot(data=df, x=x_column, y=y_column)
            plt.title("Custom Bar Chart")
        elif chart_type == "Pie":
            if color_column:
                st.warning("Pie chart does not support color differentiation.")
            else:
                st.warning("Pie chart does not support color differentiation.")
        elif chart_type == "Box":
            if color_column:
                sns.boxplot(data=df, x=x_column, y=y_column, hue=color_column)
            else:
                sns.boxplot(data=df, x=x_column, y=y_column)
            plt.title("Custom Box Plot")
        elif chart_type == "Area":
            if color_column:
                st.warning("Area chart does not support color differentiation.")
            else:
                st.warning("Area chart does not support color differentiation.")
        elif chart_type == "Histogram":
            if color_column:
                sns.histplot(data=df, x=x_column, hue=color_column, element="step")
            else:
                sns.histplot(data=df, x=x_column, element="step")
            plt.title("Custom Histogram")

        st.pyplot(plt)
    else:
        st.warning("X and Y columns should be different.")
