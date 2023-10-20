import streamlit as st
import requests

# Set a title
st.title("Currency Converter")

# Define a list of currencies and their symbols
currencies = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "AUD": "A$",
}

# User input: amount and source currency
amount = st.number_input("Enter the amount:", min_value=0.01)
source_currency = st.selectbox("Select source currency:", list(currencies.keys()))

# User selects target currency
target_currency = st.selectbox("Select target currency:", list(currencies.keys()))

# Define a function to perform currency conversion
def convert_currency(amount, source_currency, target_currency):
    # API endpoint for currency conversion
    endpoint = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"

    try:
        # Fetch exchange rates
        response = requests.get(endpoint)
        data = response.json()
        exchange_rate = data['rates'][target_currency]

        # Perform currency conversion
        converted_amount = amount * exchange_rate

        return converted_amount
    except:
        return None

# Convert currency and display the result
if st.button("Convert"):
    converted_amount = convert_currency(amount, source_currency, target_currency)

    if converted_amount is not None:
        st.write(f"{currencies[source_currency]} {amount} {source_currency} is equal to {currencies[target_currency]} {converted_amount} {target_currency}")
    else:
        st.warning("Currency conversion failed. Please try again.")
