import streamlit as st

import streamlit.components.v1 as components

# Function to convert length
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701,
        "centimeters": 100,
        "millimeters": 1000,
        "yards": 1.09361
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "kilograms": 1,
        "grams": 1000,
        "pounds": 2.20462,
        "ounces": 35.274,
        "stones": 0.157473
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value if to_unit == "Celsius" else (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
    elif from_unit == "Fahrenheit":
        return value if to_unit == "Fahrenheit" else ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
    elif from_unit == "Kelvin":
        return value if to_unit == "Kelvin" else (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)

# Function to convert volume
def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "liters": 1,
        "milliliters": 1000,
        "cubic meters": 0.001,
        "gallons": 0.264172,
        "quarts": 1.05669
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function to convert currency (USD to other currencies)
def convert_currency(value, from_currency, to_currency):
    conversion_factors = {
        "USD": 1,
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0,
        "AUD": 1.35
    }
    return value * conversion_factors[to_currency] / conversion_factors[from_currency]

# Function to convert salary to hourly
def convert_salary_to_hourly(annual_salary):
    return annual_salary / 2080

# Function to convert hourly to annual salary
def convert_hourly_to_annual(hourly_rate):
    return hourly_rate * 2080

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🌟 Unit Converter 🌟")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .stSelectbox, .stNumberInput {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Select conversion type
conversion_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature", "Volume", "Currency", "Salary"])

if conversion_type == "Length":
    units = ["meters", "kilometers", "miles", "feet", "inches", "centimeters", "millimeters", "yards"]
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    units = ["kilograms", "grams", "pounds", "ounces", "stones"]
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter value:", format="%.2f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Volume":
    units = ["liters", "milliliters", "cubic meters", "gallons", "quarts"]
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_volume(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Currency":
    units = ["USD", "EUR", "GBP", "JPY", "AUD"]
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_currency(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Salary":
    salary_type = st.selectbox("Select salary conversion type:", ["Annual to Hourly", "Hourly to Annual"])
    if salary_type == "Annual to Hourly":
        annual_salary = st.number_input("Enter annual salary:", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_salary_to_hourly(annual_salary)
            st.success(f"Annual Salary: ${annual_salary:.2f} = Hourly Rate: ${result:.2f}")
    elif salary_type == "Hourly to Annual":
        hourly_rate = st.number_input("Enter hourly rate:", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_hourly_to_annual(hourly_rate)
            st.success(f"Hourly Rate: ${hourly_rate:.2f} = Annual Salary: ${result:.2f}")