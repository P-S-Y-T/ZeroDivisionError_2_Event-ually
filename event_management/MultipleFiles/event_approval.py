import streamlit as st
from database import get_events

def event_approval():
    st.title("Event Approval Management")
    events = get_events()
    for event in events:
        event_id, title, description, date, time, venue, platform, size, fee, is_paid, is_team_event, organizer_id = event
        st.write(f"Event: {title} | Organized by: {organizer_id}")
        approve_button = st.button(f"Approve {title}")
        reject_button = st.button(f"Reject {title}")
        if approve_button:
            st.success(f"Event {title} approved!")
        if reject_button:
            st.warning(f"Event {title} rejected.")