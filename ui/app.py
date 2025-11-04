import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load model
model = joblib.load('./models/weather_classification_model.pkl')

# Define categorical and numerical columns
categorical_cols = ['Cloud Cover', 'Season', 'Location']
numerical_cols = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
                  'Atmospheric Pressure', 'UV Index', 'Visibility (km)']

# Load dataset just for options in selectbox
df = pd.read_csv('./data/weather_classification_data.csv')

# Create LabelEncoders for categorical features
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    le.fit(df[col])
    encoders[col] = le

# StandardScaler for numerical features
scaler = StandardScaler()
scaler.fit(df[numerical_cols])

# Streamlit App
st.title("Weather Classification App")

st.sidebar.header("Input Weather Features")

def user_input_features():
    inputs = {}
    for col in numerical_cols:
        inputs[col] = st.sidebar.number_input(col, value=float(df[col].mean()))
    
    for col in categorical_cols:
        options = list(df[col].unique())
        selected_val = st.sidebar.selectbox(col, options)
        inputs[col] = encoders[col].transform([selected_val])[0]
    
    input_df = pd.DataFrame([inputs])
    
    # Scale numerical features
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
    
    # Ensure correct column order
    feature_cols = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
                    'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season',
                    'Visibility (km)', 'Location']
    input_df = input_df[feature_cols]
    
    return input_df

input_df = user_input_features()

# Prediction
prediction = model.predict(input_df)[0]
prediction_proba = model.predict_proba(input_df)[0]

# Decode weather type
weather_labels = ['Cloudy', 'Rainy', 'Snowy', 'Sunny']
predicted_weather = weather_labels[prediction]

st.subheader("Predicted Weather Type")
st.write(predicted_weather)

st.subheader("Prediction Probabilities")
proba_df = pd.DataFrame([prediction_proba], columns=weather_labels)
st.write(proba_df)
