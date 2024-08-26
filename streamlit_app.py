import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # Change this to your FastAPI server URL


def register_user(
        username,
        password,
        role,
        days_pregnant,
        num_of_pregnancies,
        num_of_failed_pregnancies,
        first_time_pregnancy,
        prev_failed_pregnancies,
        med_conditions):
    response = requests.post(f"{BASE_URL}/users/", json={
        "username": username,
        "password": password,
        "role": role,
        "days_pregnant": days_pregnant,
        "num_of_pregnancies": num_of_pregnancies,
        "num_of_failed_pregnancies": num_of_failed_pregnancies,
        "first_time_pregnancy": first_time_pregnancy,
        "prev_failed_pregnancies": prev_failed_pregnancies,
        "med_conditions": med_conditions
    })
    return response.json()


def login_user(username, password):
    response = requests.post(f"{BASE_URL}/token", data={
        "username": username,
        "password": password
    })
    return response.json()


st.title("User Authentication")


st.subheader("Register")
with st.form(key='register_form'):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["woman", "doctor"])
    days_pregnant = st.number_input("Days Pregnant", min_value=0)
    num_of_pregnancies = st.number_input("Number of Pregnancies", min_value=0)
    num_of_failed_pregnancies = st.number_input("Number of Failed Pregnancies", min_value=0)
    first_time_pregnancy = st.checkbox("First Time Pregnancy")
    prev_failed_pregnancies = st.checkbox("Previous Failed Pregnancies")
    med_conditions = st.selectbox("Medical Conditions", ["diabetes", "high blood pressure", "asthma", "fertility issues", "mental health conditions", "obesity", "other"])
    submit_button = st.form_submit_button(label='Register')

    if submit_button:
        result = register_user(username, password, role, days_pregnant, num_of_pregnancies, num_of_failed_pregnancies, first_time_pregnancy, prev_failed_pregnancies, med_conditions)
        st.write(result)

st.subheader("Login")
with st.form(key='login_form'):
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    login_button = st.form_submit_button(label='Login')

    if login_button:
        result = login_user(username, password)
        st.write(result)
