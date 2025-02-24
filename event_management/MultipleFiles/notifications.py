import streamlit as st

def send_event_update(event_title, participants_emails):
    st.title(f"Send Event Update for {event_title}")
    message = st.text_area("Message")
    if st.button("Send Update"):
        for email in participants_emails:
            send_email(f"Update: {event_title}", message, email)
        st.success("Update sent successfully to participants!")