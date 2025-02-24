import streamlit as st
import sqlite3

def create_event():
    st.title("Create Event")
    title = st.text_input("Event Title")
    description = st.text_area("Event Description")
    date = st.date_input("Date")
    time = st.time_input("Time")
    venue = st.text_input("Venue")
    platform = st.text_input("Platform")
    size = st.number_input("Max Participants", min_value=1, step=1)
    fee = st.number_input("Registration Fee", min_value=0.0, step=0.01)
    is_paid = st.checkbox("Paid Event")
    is_team_event = st.checkbox("Team Event")
    organizer_id = st.text_input("Organizer ID")

    if st.button("Create Event"):
        conn = sqlite3.connect("event_management.db")
        c = conn.cursor()
        c.execute("INSERT INTO events (title, description, date, time, venue, platform, size, fee, is_paid, is_team_event, organizer_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (title, description, date, time, venue, platform, size, fee, is_paid, is_team_event, organizer_id))
        conn.commit()
        conn.close()
        st.success("Event created successfully.")