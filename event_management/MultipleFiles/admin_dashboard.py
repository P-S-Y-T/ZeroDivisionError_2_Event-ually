import streamlit as st

def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("Here you can manage the events, users, and payments.")
    if st.button("Approve Events"):
        st.write("You can approve or reject events here.")
    if st.button("View Payments"):
        st.write("You can view payment statuses here.")