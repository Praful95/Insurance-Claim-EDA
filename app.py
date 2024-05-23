import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('modelDT.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit app
st.title('Insurance Claim Prediction')

# User input
st.sidebar.title('Customer Data')
age = st.sidebar.slider('Age', min_value=18, max_value=70, step=1)
sex = st.sidebar.radio('Sex', ('Male', 'Female'))
bmi = st.sidebar.number_input('BMI', min_value=10.0, max_value=50.0, step=0.01, format="%.2f")
children = st.sidebar.number_input('Children', min_value=0, max_value=10, step=1)
smoker = st.sidebar.radio('Smoker', ('Yes', 'No'))
region = st.sidebar.slider('Region', min_value=1, max_value=4, step=1)
charges = st.sidebar.number_input('Charges', min_value=0, max_value=100000, step=1)
insurancetaken = st.sidebar.radio('Insurance Taken', ('Yes', 'No'))

# Convert user input to DataFrame
user_data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == 'Male' else 0],
    'bmi': [bmi],
    'children': [children],
    'smoker': [1 if smoker == 'Yes' else 0],
    'region': [region],
    'charges': [charges],
    'insurancetaken': [1 if insurancetaken == 'Yes' else 0]
})

# Convert numerical values to corresponding labels
user_data_display = user_data.copy()
user_data_display['sex'] = 'Male' if user_data_display['sex'].iloc[0] == 1 else 'Female'
user_data_display['smoker'] = 'Yes' if user_data_display['smoker'].iloc[0] == 1 else 'No'
user_data_display['insurancetaken'] = 'Yes' if user_data_display['insurancetaken'].iloc[0] == 1 else 'No'

# Display user input and prediction result
st.subheader('User Input Data')
st.write(user_data_display)

st.subheader('Prediction Result')
# Prediction
if st.sidebar.button('Predict'):
    prediction = loaded_model.predict(user_data)
    if prediction[0] == 1:
        result = 'Insurance Claim will be Taken'
        st.success(result)
    else:
        result = 'Insurance Claim will not be Taken'
        st.error(result)