import streamlit as st
import plotly.express as px
import pandas as pd

# Set a title and a subtitle
st.title("Custom Chart App")
st.subheader("Create a custom chart with user-provided data")

# Create a sidebar with user input for chart type
chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter", "Line", "Bar", "Pie", "Box", "Area", "Histogram"])

# Create a file uploader for CSV files
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Define a list of predefined color palettes
color_palettes = {
    "Default": px.colors.qualitative.Plotly,
    "Set1": px.colors.qualitative.Set1,
    "Set2": px.colors.qualitative.Set2,
    "Set3": px.colors.qualitative.Set3,
    "Dark24": px.colors.qualitative.Dark24,
    "Pastel1": px.colors.qualitative.Pastel1,
    "Viridis": px.colors.sequential.Viridis,
    "Blues": px.colors.sequential.Blues,
    "YlOrRd": px.colors.sequential.YlOrRd,
}

# Create a selectbox for selecting a color palette
selected_palette = st.sidebar.selectbox("Select Color Palette", list(color_palettes.keys()))

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
        # Create an interactive chart based on the selected chart type with color differentiation and custom color palette
        if chart_type == "Scatter":
            fig = px.scatter(df, x=x_column, y=y_column, color=color_column, title="Custom Scatter Plot", color_discrete_sequence=color_palettes[selected_palette])
        elif chart_type == "Line":
            fig = px.line(df, x=x_column, y=y_column, color=color_column, title="Custom Line Chart", color_discrete_sequence=color_palettes[selected_palette])
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_column, y=y_column, color=color_column, title="Custom Bar Chart", color_discrete_sequence=color_palettes[selected_palette])
        elif chart_type == "Pie":
            fig = px.pie(df, names=x_column, values=y_column, title="Custom Pie Chart", color_discrete_sequence=color_palettes[selected_palette])
        elif chart_type == "Box":
            fig = px.box(df, x=x_column, y=y_column, color=color_column, title="Custom Box Plot", color_discrete_sequence=color_palettes[selected_palette])
        elif chart_type == "Area":
            fig = px.area(df, x=x_column, y=y_column, color=color_column, title="Custom Area Chart", color_discrete_sequence=color_palettes[selected_palette])
        elif chart_type == "Histogram":
            fig = px.histogram(df, x=x_column, y=y_column, color=color_column, title="Custom Histogram", color_discrete_sequence=color_palettes[selected_palette])

        # Display the interactive chart
        st.plotly_chart(fig)
    else:
        st.warning("X and Y columns should be different.")
