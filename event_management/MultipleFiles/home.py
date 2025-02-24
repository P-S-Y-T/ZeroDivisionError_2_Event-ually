import streamlit as st
import sqlite3
from event_details import view_event_details  # Import the function to view event details

def display_homepage():
    st.title("Upcoming Events")
    try:
        conn = sqlite3.connect("event_management.db")
        c = conn.cursor()
        c.execute("SELECT id, title, date FROM events")
        events = c.fetchall()
        conn.close()

        if events:
            for event in events:
                st.subheader(event[1])  # Event title
                st.write("Date:", event[2])
                if st.button(f"View Details {event[0]}"):
                    st.session_state['selected_event'] = event[0]  # Store selected event ID
                    st.experimental_rerun()  # Rerun the app to show details
        else:
            st.info("No upcoming events.")
    except Exception as e:
        st.error(f"An error occurred: {e}")