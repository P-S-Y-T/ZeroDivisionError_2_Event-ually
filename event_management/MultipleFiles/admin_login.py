import streamlit as st
from database import get_user_by_email

def admin_login():
    st.title("Admin Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user_by_email(email)
        if user and user[3] == "admin":
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials or unauthorized access.")