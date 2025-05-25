import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model_path = 'random_forest_regressor_model.pkl'
model = joblib.load(model_path)

# Encoding mappings
rainfall_mapping = {'moderate': 2, 'low': 1, 'high': 0}
soil_type_mapping = {'sandy': 3, 'silty': 4, 'clay': 0, 'peaty': 2, 'loamy': 1}
drainage_mapping = {'poor': 2, 'moderate': 1, 'good': 0}
crop_mapping = {'rice': 2, 'wheat': 4, 'soybean': 3, 'cotton': 0, 'maize': 1}
growth_stage_mapping = {'flowering': 0, 'fruiting': 1, 'vegetative': 5, 'seedling': 4, 'reproductive': 3, 'maturity': 2}

# Function to preprocess user inputs
def preprocess_input(data):
    data['rainfall_pattern'] = rainfall_mapping[data['rainfall_pattern']]
    data['soil_type'] = soil_type_mapping[data['soil_type']]
    data['drainage_properties'] = drainage_mapping[data['drainage_properties']]
    data['crop_type'] = crop_mapping[data['crop_type']]
    data['growth_stage'] = growth_stage_mapping[data['growth_stage']]
    return np.array(list(data.values())).reshape(1, -1)

# Streamlit App
st.title("Predicting Water Usage in Agriculture using Big data tools")
st.write("This application predicts the optimal water requirement for different crops based on environmental and soil properties.")

# User Inputs
st.sidebar.header("Input Features")

# Numerical inputs
temperature = st.sidebar.slider("Temperature (°C):", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
humidity = st.sidebar.slider("Humidity (%):", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
wind_speed = st.sidebar.slider("Wind Speed (m/s):", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
evapotranspiration = st.sidebar.slider("Evapotranspiration (mm/day):", min_value=0.0, max_value=10.0, value=3.0, step=0.1)
soil_moisture_levels = st.sidebar.slider("Soil Moisture Levels (%):", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
water_retention_capacity = st.sidebar.slider("Water Retention Capacity (%):", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
crop_water_requirement = st.sidebar.slider("Actual Water Requirement (mm/day)):", min_value=0.0, max_value=25.0, value=10.0, step=0.1)

# Categorical inputs
rainfall_pattern = st.sidebar.selectbox("Rainfall Pattern:", list(rainfall_mapping.keys()))
soil_type = st.sidebar.selectbox("Soil Type:", list(soil_type_mapping.keys()))
drainage_properties = st.sidebar.selectbox("Drainage Properties:", list(drainage_mapping.keys()))
crop_type = st.sidebar.selectbox("Crop Type:", list(crop_mapping.keys()))
growth_stage = st.sidebar.selectbox("Growth Stage:", list(growth_stage_mapping.keys()))

# Prediction
if st.sidebar.button("Predict Water Requirement"):
    input_data = {
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'evapotranspiration': evapotranspiration,
        'soil_moisture_levels': soil_moisture_levels,
        'water_retention_capacity': water_retention_capacity,
        'rainfall_pattern': rainfall_pattern,
        'soil_type': soil_type,
        'drainage_properties': drainage_properties,
        'crop_type': crop_type,
        'growth_stage': growth_stage,
        'crop_water_requirement':crop_water_requirement
    }
    processed_data = preprocess_input(input_data)
    prediction = model.predict(processed_data)[0]


    st.write("### Predicted Water Requirement")
    st.success(f"The predicted water requirement is **{prediction:.2f} mm/day**.")

    st.header("Optimization Suggestions")

    suggestions = []

    # Check soil type
    if soil_type == "Sandy":
        suggestions.append("Consider improving soil structure by adding organic matter or compost to enhance water retention.")

    # Check evapotranspiration
    if evapotranspiration > 8.0:
        suggestions.append("High evapotranspiration detected. Use mulching to reduce evaporation and conserve soil moisture.")

    # Check soil moisture
    if soil_moisture_levels < 15.0:
        suggestions.append("Low soil moisture detected. Ensure proper irrigation scheduling to maintain adequate levels.")

    # Check water retention
    if water_retention_capacity < 20.0:
        suggestions.append("Low water retention capacity. Incorporate soil amendments to improve retention.")

    # Check drainage
    if drainage_properties=='good':
        suggestions.append("Poor drainage detected. Improve soil aeration or use soil conditioners to balance drainage.")

    # Display suggestions
    if suggestions:
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.write("✅ All parameters are well-balanced for optimal water usage!")


# Footer
st.write("---")

import streamlit as st
import datetime

# Get current year dynamically
current_year = datetime.datetime.now().year

st.markdown(f"""
    <style>
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #262730;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 16px;
            font-family: Arial, sans-serif;
            box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.2);
        }}
        .footer a {{
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
            color: #FFD700;
            align-items: center;
        }}
        .footer img {{
            width: 20px;
            height: 20px;
            vertical-align: middle;
            margin-right: 5px;
            filter: invert(70%) sepia(90%) saturate(500%) hue-rotate(180deg);
        }}
    </style>
    <div class="footer">
        <p>© {current_year} Aditya Manwatkar |  
        <a href="https://github.com/Aditya-Manwatkar" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg"> GitHub
        </a> |  
        <a href="https://www.linkedin.com/in/aditya-manwatkar/" target="_blank">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg"> LinkedIn
        </a>
        </p>
    </div>
""", unsafe_allow_html=True)
