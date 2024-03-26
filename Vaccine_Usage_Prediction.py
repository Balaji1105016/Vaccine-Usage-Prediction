import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Reading the Pickle file:
with open('knn_model.pkl', 'rb') as f:
    knn = pickle.load(f)

# Image Details:
st.title("Vaccine Usage Prediction")
st.subheader("By")
img_path = r"C:\Users\Balaji\Music\Personal_Pic\Balaji_pic.jpeg"
img = Image.open(img_path)
st.image(img, caption="""Name: BALAJI BALAKRISHNAN(Data Engineer)\n
         
                         Linkedin URL: www.linkedin.com/in/balaji-balakrishnan-34471b167""", use_column_width=True)

# Login and Logout Page:
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
    
username = st.text_input("User Name")
password = st.text_input("Password",type = 'password')
if st.button("Login"):
    if username == "Balaji" and password == "Balaji@123":
        st.session_state.login_status = True
        st.success("Login Successful!")
    
    else:
        st.session_state.login_status = False
        st.error("Invalid Credentials. Please try again.")

if st.session_state.login_status:      
    logout = st.sidebar.button("Logout")
    if logout:
        if 'login_status' in st.session_state:
            st.session_state.login_status = False
            st.experimental_rerun()

    st.title("Vaccine Usage Prediction")
    st.success("Note: This Application Will Be Helpful For Making A Best Prediction About the Recommendation of H1N1 Vaccination")

    H1N1_Worry = st.selectbox("H1N1_Worry Input", (0, 1, 2, 3))
    chronic_medic_condition = st.selectbox("Chronic Medic Condition Input", (0, 1))
    is_H1N1_risky = st.selectbox("Is H1N1 Risky Input", (1, 2, 3, 4, 5))
    sick_from_h1n1_vacc = st.selectbox("Sick from H1N1 Vacc Input", (1, 2, 3, 4, 5))
    is_h1n1_vacc_effective = st.selectbox("Is H1N1 Vacc Effective Input", (1, 2, 3, 4, 5))
    dr_recc_h1n1_vacc = st.selectbox("Dr Recc H1N1 Vacc Input", (0, 1))
    sex = st.selectbox("Male or Female", (1,2))
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

        # Making prediction using knn
        prediction = knn.predict(input_data)

        st.subheader("H1N1 Vaccine Recommendation")
        if prediction[0]==1:
            st.success("The H1N1 Vaccine is recommended")
        else:
            st.warning("The H1N1 Vaccine is not recommended")
        
    st.success("""
        1) h1n1_worry - Worry about the h1n1 flu(0,1,2,3) 0=Not worried at all, 1=Not very worried, 2=Somewhat worried, 3=Very worried.\n
        2) chronic_medic_condition - Has any chronic medical condition - (0,1).\n
        3) is_h1n1_risky	- What respondents think about the risk of getting ill with h1n1 in the absence of the vaccine- (1,2,3,4,5)- (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=don’t know if it is risky or not, 4=Thinks it is a somewhat high risk, 5=Thinks it is very highly risky).\n
        4) sick_from_h1n1_vacc - Does respondent worry about getting sick by taking the h1n1 vaccine - (1,2,3,4,5)- (1=Respondent not worried at all, 2=Respondent is not very worried, 3=Doesn't know, 4=Respondent is somewhat worried, 5Respondent is very worried).\n
        5) is_h1n1_vacc_effective - Does respondent think that the h1n1 vaccine is effective - (1,2,3,4,5)- (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn't know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective).\n
        6) dr_recc_h1n1_vacc	- Doctor has recommended h1n1 vaccine - (0,1).\n
        7) sex	- Respondent's sex - (Female, Male) - 1 - Female,2 - Male.\n
    """)
    
        # (1,1,2,1,5,1,1) - 1
        # (1,1,2,1,5,1,0) - 1
        # (1,1,2,1,4,1,1) - 1
        # (1,1,2,3,4,1,1) - 1
