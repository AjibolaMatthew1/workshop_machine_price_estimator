import streamlit as st
import numpy as np

# Define the coefficients for each scenario
coefficients = {
    'All Variables': {
        'Initial Cost': 0.00001,
        'Area Occupied': 0.05,
        'Power Rating': 0.003,
        'Time Spent': 150,
        'Workpieces': 5,
        'Operators': 50,
        'Ventilation Cost': 0.1,
        'Cleaning Cost': 0.08,
        'Waste Management Cost': 0.07,
        'Toilet Usage Cost': 0.02
    },
    'Excluding Workpieces': {
        'Initial Cost': 0.000012,
        'Area Occupied': 0.055,
        'Power Rating': 0.004,
        'Time Spent': 120,
        'Operators': 55,
        'Ventilation Cost': 0.1,
        'Cleaning Cost': 0.09,
        'Waste Management Cost': 0.08,
        'Toilet Usage Cost': 0.03
    },
    'Excluding Operators': {
        'Initial Cost': 0.000011,
        'Area Occupied': 0.06,
        'Power Rating': 0.0035,
        'Time Spent': 110,
        'Workpieces': 6,
        'Ventilation Cost': 0.12,
        'Cleaning Cost': 0.1,
        'Waste Management Cost': 0.09,
        'Toilet Usage Cost': 0.03
    },
    'Excluding Workpieces and Operators': {
        'Initial Cost': 0.000013,
        'Area Occupied': 0.065,
        'Power Rating': 0.0045,
        'Time Spent': 130,
        'Ventilation Cost': 0.15,
        'Cleaning Cost': 0.12,
        'Waste Management Cost': 0.1,
        'Toilet Usage Cost': 0.035
    }
}

# Define the ranges for each machine type
machine_ranges = {
    'Lathe Machine': {
        'Initial Cost': [1500000, 3800000],
        'Area Occupied': [50, 500],
        'Power Rating': [15000, 22000],
        'Time Spent': [60, 720],
        'Workpieces': [5, 30],
        'Operators': [2, 10],
        'Ventilation Cost': [5000, 15000],
        'Cleaning Cost': [3500, 10000],
        'Waste Management Cost': [3500, 10000],
        'Toilet Usage Cost': [3500, 10000]
    },
    'Milling Machine': {
        'Initial Cost': [5000000, 40000000],
        'Area Occupied': [50, 500],
        'Power Rating': [20000, 40000],
        'Time Spent': [60, 720],
        'Workpieces': [10, 50],
        'Operators': [1, 5],
        'Ventilation Cost': [7000, 10000],
        'Cleaning Cost': [4000, 15000],
        'Waste Management Cost': [4000, 15000],
        'Toilet Usage Cost': [3500, 10000]
    },
    'Drilling Machine': {
        'Initial Cost': [1500000, 4000000],
        'Area Occupied': [50, 500],
        'Power Rating': [10000, 25000],
        'Time Spent': [60, 720],
        'Workpieces': [5, 30],
        'Operators': [2, 5],
        'Ventilation Cost': [5000, 15000],
        'Cleaning Cost': [3500, 10000],
        'Waste Management Cost': [3500, 10000],
        'Toilet Usage Cost': [3500, 10000]
    },
    'Grounding Machine': {
        'Initial Cost': [1500000, 5000000],
        'Area Occupied': [50, 500],
        'Power Rating': [5000, 20000],
        'Time Spent': [60, 720],
        'Workpieces': [5, 30],
        'Operators': [2, 5],
        'Ventilation Cost': [5000, 15000],
        'Cleaning Cost': [3500, 10000],
        'Waste Management Cost': [3500, 10000],
        'Toilet Usage Cost': [3500, 10000]
    }
}

# Function to calculate price based on inputs
def calculate_price(scenario, machine_type, input_data):
    coeff = coefficients[scenario]
    ranges = machine_ranges[machine_type]

    price = 0
    price += coeff['Initial Cost'] * input_data['Initial Cost']
    price += coeff['Area Occupied'] * input_data['Area Occupied']
    price += coeff['Power Rating'] * input_data['Power Rating']
    price += coeff['Time Spent'] * input_data['Time Spent']
    if 'Workpieces' in coeff:
        price += coeff['Workpieces'] * input_data['Workpieces']
    if 'Operators' in coeff:
        price += coeff['Operators'] * input_data['Operators']
    price += coeff['Ventilation Cost'] * input_data['Ventilation Cost']
    price += coeff['Cleaning Cost'] * input_data['Cleaning Cost']
    price += coeff['Waste Management Cost'] * input_data['Waste Management Cost']
    price += coeff['Toilet Usage Cost'] * input_data['Toilet Usage Cost']

    return max(20000, min(300000, price))  # Clamping the price between 20,000 and 300,000

# Streamlit UI
st.title("Workshop Machine Price Estimator")

st.write("""
This tool estimates the price of various workshop machines based on assigned coefficients. The coefficients used in this model are assigned arbitrarily for illustrative purposes.
""")

# Scenario selection
scenario = st.selectbox("Select Scenario", ["All Variables", "Excluding Workpieces", "Excluding Operators", "Excluding Workpieces and Operators"])

# Machine type selection
machine_type = st.selectbox("Select Machine Type", ["Lathe Machine", "Milling Machine", "Drilling Machine", "Grounding Machine"])

# Get the input ranges for the selected machine
ranges = machine_ranges[machine_type]

# Collect input data
input_data = {
    'Initial Cost': st.number_input(f"Initial Cost (₦)", min_value=ranges['Initial Cost'][0], max_value=ranges['Initial Cost'][1]),
    'Area Occupied': st.number_input(f"Area Occupied (m²)", min_value=ranges['Area Occupied'][0], max_value=ranges['Area Occupied'][1]),
    'Power Rating': st.number_input(f"Power Rating (Watts)", min_value=ranges['Power Rating'][0], max_value=ranges['Power Rating'][1]),
    'Time Spent': st.number_input(f"Time Spent (minutes)", min_value=ranges['Time Spent'][0], max_value=ranges['Time Spent'][1]),
    'Workpieces': st.number_input(f"Workpieces (units)", min_value=ranges['Workpieces'][0], max_value=ranges['Workpieces'][1]) if "Workpieces" in coefficients[scenario] else 0,
    'Operators': st.number_input(f"Operators (persons)", min_value=ranges['Operators'][0], max_value=ranges['Operators'][1]) if "Operators" in coefficients[scenario] else 0,
    'Ventilation Cost': st.number_input(f"Ventilation Cost (₦)", min_value=ranges['Ventilation Cost'][0], max_value=ranges['Ventilation Cost'][1]),
    'Cleaning Cost': st.number_input(f"Cleaning Cost (₦)", min_value=ranges['Cleaning Cost'][0], max_value=ranges['Cleaning Cost'][1]),
    'Waste Management Cost': st.number_input(f"Waste Management Cost (₦)", min_value=ranges['Waste Management Cost'][0], max_value=ranges['Waste Management Cost'][1]),
    'Toilet Usage Cost': st.number_input(f"Toilet Usage Cost (₦)", min_value=ranges['Toilet Usage Cost'][0], max_value=ranges['Toilet Usage Cost'][1])
}

# Calculate and display price
if st.button("Calculate Price"):
    price = calculate_price(scenario, machine_type, input_data)
    st.success(f"The estimated price is: ₦{price:,.2f}")
