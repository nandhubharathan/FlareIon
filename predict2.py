import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained RandomForest model
model = joblib.load('rf_flare_predictor_regressor.pkl')

# Load the columns from the preprocessed dataset (updated_dataset.csv)
conv_df = pd.read_csv('conv3.csv')
model_columns = conv_df.columns.drop('Time_Between_Flares')  # These are the columns the model expects

# Set up the Streamlit app
st.title('Flare-Ion')
st.write('This application predicts the occurrence of the next flare in days based on your input and calculates severity.')

# Create a form for user input
st.subheader("Input Patient Data")

# Example of input fields for various features
age = st.number_input('Age', min_value=0, max_value=120, value=30)
gender = st.selectbox('Gender', ('Male', 'Female'))
Disease_Type = st.selectbox('Disease Type', (
    'Addisons Disease', 'Graves Disease', 'Hashimotos Thyroiditis', 
    'Lupus', 'Multiple Sclerosis', 'Myasthenia Gravis', 
    'Psoriasis', 'Rheumatoid Arthritis', 'Sjogren Syndrome', 
    'Type 1 Diabetes'))
Genetic_Markers = st.selectbox('Genetic Markers', (
    'AChR', 'CTLA4', 'HLA DQB1', 'HLA DR3', 
    'HLA DRB1', 'IL12B', 'IL7R', 'STAT4', 'TSHR'))
Biomarkers = st.selectbox('Bio Markers', (
    'Elevated Acetylcholine Receptor Antibodies', 'Elevated IL 6', 
    'Elevated TSI', 'High ANA', 'High Blood Sugar', 
    'High CRP', 'High IL 17', 'High RF', 
    'High TPO Antibodies', 'Low Cortisol'))
Environmental_Factors = st.selectbox('Environmental Factors', (
    'Air Pollution', 'High Altitude Living', 'High Stress Job', 
    'Low Iodine Intake', 'Rural Area', 'Smoking', 'Urban Living'))
Medical_History = st.selectbox('Medical History', (
    'Asthma', 'High Blood Pressure', 'Hypertension', 
    'Obesity', 'Type 2 Diabetes'))

# When the user clicks the 'Predict' button
if st.button('Predict Next Flare'):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Disease_Type': [Disease_Type],
        'Genetic_Markers': [Genetic_Markers],
        'Biomarkers': [Biomarkers],
        'Environmental_Factors': [Environmental_Factors],
        'Medical_History': [Medical_History]
    })

    # One-Hot Encoding for multi-category columns
    multi_category_columns = ['Gender', 'Disease_Type', 'Genetic_Markers', 'Biomarkers', 'Environmental_Factors', 'Medical_History']
    input_data_encoded = pd.get_dummies(input_data, columns=multi_category_columns)

    # Add missing columns that the model expects (set them to 0 if missing)
    for col in model_columns:
        if col not in input_data_encoded.columns:
            input_data_encoded[col] = 0

    # Ensure the input data has the same column order as the model expects
    input_data_encoded = input_data_encoded[model_columns]

    # Display the encoded input data (optional)
    st.write("Patient Data (encoded):")
    st.write(input_data_encoded)

    # Make predictions using the model
    prediction = model.predict(input_data_encoded)

    # Round the prediction to the nearest integer (to get whole number days)
    prediction_rounded = int(round(prediction[0]))

    # Calculate severity based on input data
    severity_score = 0
    reasons_for_severity = []

    # Example severity logic (expand based on your data):
    genetic_markers = input_data['Genetic_Markers'][0]
    if genetic_markers == 'HLA DR3':
        severity_score += 2
        reasons_for_severity.append("Genetic marker HLA DR3 is associated with increased severity.")
    elif genetic_markers == 'HLA DRB1':
        severity_score += 2
        reasons_for_severity.append("Genetic marker HLA DRB1 is linked with higher flare risk.")
    elif genetic_markers == 'IL12B':
        severity_score += 1
        reasons_for_severity.append("Genetic marker IL12B indicates a slightly increased risk.")

    biomarkers = input_data['Biomarkers'][0]
    if biomarkers == 'Elevated IL 6':
        severity_score += 2
        reasons_for_severity.append("Elevated IL 6 is a known biomarker for inflammation, contributing to severity.")
    elif biomarkers == 'High ANA':
        severity_score += 3
        reasons_for_severity.append("High ANA levels are directly linked to auto-immune severity.")

    medical_history = input_data['Medical_History'][0]
    if medical_history == 'Asthma':
        severity_score += 1
        reasons_for_severity.append("Asthma history adds mild severity risk.")
    elif medical_history == 'Obesity':
        severity_score += 2
        reasons_for_severity.append("Obesity significantly contributes to flare severity.")

    # Determine severity level based on severity score
    if severity_score >= 5:
        severity_level = "Severe"
    elif 2 <= severity_score < 5:
        severity_level = "Moderately Severe"
    else:
        severity_level = "Less Severe"

    # Generate explanation for flare-up risk
    reasons_for_flare_up = []
    if biomarkers == 'High ANA' or biomarkers == 'Elevated IL 6':
        reasons_for_flare_up.append(f"Biomarkers such as {biomarkers} indicate an immune system imbalance, which can trigger a flare-up.")
    if Environmental_Factors == 'High Stress Job':
        reasons_for_flare_up.append("High stress levels can trigger an immune response and lead to a flare-up.")
    if medical_history in ['Asthma', 'Obesity', 'Type 2 Diabetes']:
        reasons_for_flare_up.append(f"Your medical history, including {medical_history}, contributes to the likelihood of a flare-up.")

    # Display the results
    st.subheader(f"The flare is predicted to occur in {prediction_rounded} days.")
    st.subheader(f"Severity Level: {severity_level}")

    # Display reasons for severity
    st.write("**Reasons for Severity:**")
    for reason in reasons_for_severity:
        st.write(f"- {reason}")

    # Display reasons for flare-up likelihood
    st.write("**Reasons why a flare-up may happen:**")
    for reason in reasons_for_flare_up:
        st.write(f"- {reason}")
