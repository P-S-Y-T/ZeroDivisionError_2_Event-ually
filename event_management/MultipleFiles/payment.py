import streamlit as st
from payment_gateway import process_payment

def make_payment(user_id, event_id, amount):
    st.title("Make Payment")
    st.write("Event ID:", event_id)
    st.write("Amount:", amount)

    if st.button("Pay Now"):
        success = process_payment(user_id, event_id, amount)
        if success:
            st.success("Payment successful!")
        else:
            st.error("Payment failed. Please try again.")