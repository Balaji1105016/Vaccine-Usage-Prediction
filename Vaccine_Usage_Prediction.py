import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('knn_model.pkl', 'rb') as f:
    knn = pickle.load(f)

# Streamlit app
st.title("Vaccine Usage Prediction")
st.success("Note: This Application Will Be Helpful For Making A Best Prediction About the Recommendation of H1N1 Vaccination")

H1N1_Worry = st.selectbox("H1N1_Worry Input", (0, 1, 2, 3))
chronic_medic_condition = st.selectbox("Chronic Medic Condition Input", (0, 1))
is_H1N1_risky = st.selectbox("Is H1N1 Risky Input", (1, 2, 3, 4, 5))
sick_from_h1n1_vacc = st.selectbox("Sick from H1N1 Vacc Input", (1, 2, 3, 4, 5))
is_h1n1_vacc_effective = st.selectbox("Is H1N1 Vacc Effective Input", (1, 2, 3, 4, 5))
dr_recc_h1n1_vacc = st.selectbox("Dr Recc H1N1 Vacc Input", (0, 1))
sex = st.selectbox("Male or Female", (0, 1))
submit_button = st.button("Submit")

if submit_button:
    input_data = pd.DataFrame({
        'h1n1_worry': [H1N1_Worry],
        'chronic_medic_condition': [chronic_medic_condition],
        'is_h1n1_risky': [is_H1N1_risky],
        'sick_from_h1n1_vacc': [sick_from_h1n1_vacc],
        'is_h1n1_vacc_effective': [is_h1n1_vacc_effective],
        'dr_recc_h1n1_vacc': [dr_recc_h1n1_vacc],
        'sex': [sex]
    })

    # Make prediction
    prediction = knn.predict(input_data)

    st.subheader("H1N1 Vaccine Recommendation")
    if prediction[0]==1:
        st.success("The H1N1 Vaccine is recommended")
    else:
        st.warning("The H1N1 Vaccine is not recommended")

    
    # (1,1,2,1,5,1,1) - 1
    # (1,1,2,1,5,1,0) - 1
    

    
