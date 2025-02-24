import streamlit as st
from home import display_homepage
from event_details import view_event_details
from payment import make_payment
from registrations import register_for_event
from event_creation import create_event
from event_management import manage_events
from notifications import send_event_update
from posts_and_polls import manage_posts_and_polls

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Event Details", "Register", "Payment", "Create Event", "Manage Events", "Notify Participants", "Manage Posts and Polls"])

    if page == "Home":
        display_homepage()
    elif page == "Event Details":
        event_id = st.sidebar.text_input("Event ID")
        if event_id:
            view_event_details(event_id)
    elif page == "Register":
        user_id = st.sidebar.text_input("User  ID")
        event_id = st.sidebar.text_input("Event ID")
        if user_id and event_id:
            register_for_event(user_id, event_id)
    elif page == "Payment":
        user_id = st.sidebar.text_input("User  ID")
        event_id = st.sidebar.text_input("Event ID")
        amount = st.sidebar.number_input("Amount", min_value=0.0, step=0.01)
        if user_id and event_id and amount > 0:
            make_payment(user_id, event_id, amount)
    elif page == "Create Event":
        create_event()
    elif page == "Manage Events":
        manage_events()
    elif page == "Notify Participants":
        event_id = st.sidebar.text_input("Event ID")
        message = st.sidebar.text_area("Message")
        if event_id and message:
            send_event_update(event_id, message)
    elif page == "Manage Posts and Polls":
        event_id = st.sidebar.text_input("Event ID")
        if event_id:
            manage_posts_and_polls(event_id)

if __name__ == "__main__":
    main()