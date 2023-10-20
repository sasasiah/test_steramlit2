import streamlit as st
import requests

# Set a title
st.title("Weather App")

# User input: city name
city_name = st.text_input("Enter a city name:")

# Custom CSS styles for text input and button
st.markdown(
    """
    <style>
    .stTextInput {background-color: #F4F4F4; border: 2px solid #1E90FF; color: #333;}
    .stButton {background-color: #1E90FF; color: white; border: none;}
    .stButton:hover {background-color: #1669b2;}
    </style>
    """,
    unsafe_allow_html=True
)

# Custom background image
st.markdown(
    """
    <style>
    body {
    background-image: url('https://cdn.pixabay.com/photo/2016/10/25/14/03/clouds-1768967_1280.jpg');
    background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define a function to fetch weather data from the OpenWeatherMap API
def get_weather(city_name):
    try:
        api_key = "6183a695e0be3f9d1e3fd456fab42ac1"  # Replace with your OpenWeatherMap API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        # Fetch weather data
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            # Extract and format weather information
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            return {
                "description": weather_description,
                "temperature": temperature - 273.15,  # Convert from Kelvin to Celsius
                "humidity": humidity,
            }
        else:
            return None
    except Exception as e:
        return None

# Display weather information
if st.button("Get Weather"):
    weather_data = get_weather(city_name)

    if weather_data is not None:
        st.write(f"Weather in {city_name}:")
        st.write(f"Description: {weather_data['description']}")
        st.write(f"Temperature: {weather_data['temperature']:.2f}°C")
        st.write(f"Humidity: {weather_data['humidity']}%")
    else:
        st.warning("Weather data not available for the specified city. Please check the city name or try again later.")

