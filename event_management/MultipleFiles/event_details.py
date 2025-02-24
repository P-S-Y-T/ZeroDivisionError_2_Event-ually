import streamlit as st
import sqlite3

def view_event_details(event_id):
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    event = c.fetchone()
    conn.close()

    if event:
        st.title(event[1])  # Event title
        st.write(event[2])  # Event description
        st.write("Date:", event[3])
        st.write("Time:", event[4])
        st.write("Venue:", event[5])
        st.write("Platform:", event[6])
        st.write("Registration Fee:", event[7])
        st.write("Max Participants:", event[8])
    else:
        st.error("Event not found.")