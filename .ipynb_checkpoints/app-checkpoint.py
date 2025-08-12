import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("co2_model.pkl")

st.title("🚗 Carbon Footprint Estimator")
st.write("Estimate your vehicle's CO₂ emissions and lifetime environmental impact.")

# User inputs
make = st.text_input("Make", "BMW")
vehicle_class = st.selectbox("Vehicle Class", ["SUV - Small", "SUV - Large", "Mid-size", "Compact"])
engine_size = st.number_input("Engine Size (L)", 0.0, 8.0, 2.0)
cylinders = st.number_input("Cylinders", 2, 16, 4)
transmission = st.text_input("Transmission", "A8")
fuel_type = st.selectbox("Fuel Type", ["Z", "D", "X", "E", "N"])
city_l = st.number_input("City L/100km", 0.0, 30.0, 10.5)
hwy_l = st.number_input("Highway L/100km", 0.0, 30.0, 8.0)

annual_mileage = st.number_input("Annual Mileage (km)", 0, 50000, 15000)
years = st.number_input("Years of Use", 1, 30, 5)

if st.button("Predict CO₂ Emissions"):
    input_data = pd.DataFrame([{
        "Make": make,
        "Vehicle_Class": vehicle_class,
        "Engine_Size": engine_size,
        "Cylinders": cylinders,
        "Transmission": transmission,
        "Fuel_Type": fuel_type,
        "City_L_per_100km": city_l,
        "Hwy_L_per_100km": hwy_l
    }])
    
    predicted_co2 = model.predict(input_data)[0]
    lifetime_emissions = (predicted_co2 * annual_mileage * years) / 1000

    st.success(f"Predicted CO₂ per km: {predicted_co2:.2f} g/km")
    st.info(f"Estimated lifetime emissions: {lifetime_emissions:.2f} kg CO₂")
