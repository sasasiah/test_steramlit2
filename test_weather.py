import streamlit as st
import requests

# Set a title
st.title("Weather App")

# User input: city name
city_name = st.text_input("Enter a city name:")

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
            icon = data["weather"][0]["icon"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            return {
                "description": weather_description,
                "icon": icon,
                "temperature": temperature - 273.15,  # Convert from Kelvin to Celsius
                "humidity": humidity,
            }
        else:
            return None
    except Exception as e:
        return None

# Define weather icons mapping
weather_icons = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "🌥️",
    "broken clouds": "☁️",
    "shower rain": "🌦️",
    "rain": "🌧️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️"
}
# Display weather information with larger font
if st.button("Get Weather"):
    weather_data = get_weather(city_name)

    if weather_data is not None:
        st.subheader(f"Weather in {city_name}:")

        # Larger font size using Markdown <h1> tag
        st.write(f"**<h1>Description:</h1>** {weather_data['description']} {weather_icons.get(weather_data['description'], '')}")

        # Slightly smaller font size using Markdown <h2> tag
        st.write(f"**<h2>Temperature:</h2>** **{weather_data['temperature']:.2f}°C**")
        st.write(f"**<h2>Humidity:</h2>** **{weather_data['humidity']}%**")
    else:
        st.warning("Weather data not available for the specified city. Please check the city name or try again later.")








