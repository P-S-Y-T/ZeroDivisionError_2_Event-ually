import streamlit as st
import sqlite3

def manage_events():
    st.title("Manage Events")
    organizer_id = st.text_input("Organizer ID")
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE organizer_id = ?", (organizer_id,))
    events = c.fetchall()
    conn.close()

    if events:
        for event in events:
            st.subheader(event[1])  # Event title
            st.write(event[2])     # Event description
            if st.button(f"Edit {event[1]}"):
                st.warning("Edit functionality not yet implemented.")
            if st.button(f"Delete {event[1]}"):
                conn = sqlite3.connect("event_management.db")
                c = conn.cursor()
                c.execute("DELETE FROM events WHERE id = ?", (event[0],))
                conn.commit()
                conn.close()
                st.success("Event deleted.")
    else:
        st.info("No events found for this organizer.")