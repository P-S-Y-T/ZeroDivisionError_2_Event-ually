import streamlit as st
import sqlite3

def register_for_event(user_id, event_id):
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()
    c.execute("SELECT * FROM registrations WHERE user_id = ? AND event_id = ?", (user_id, event_id))
    registration = c.fetchone()

    if registration:
        st.warning("You are already registered for this event.")
    else:
        c.execute("INSERT INTO registrations (user_id, event_id) VALUES (?, ?)", (user_id, event_id))
        conn.commit()
        st.success("Successfully registered for the event.")

    conn.close()