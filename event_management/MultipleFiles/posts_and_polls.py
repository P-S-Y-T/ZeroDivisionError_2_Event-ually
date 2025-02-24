import streamlit as st
import sqlite3

def manage_posts_and_polls(event_id):
    st.title("Manage Posts and Polls")
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()

    # Create Post
    st.subheader("Create Post")
    post_content = st.text_area("Post Content")
    if st.button("Add Post"):
        c.execute("INSERT INTO posts (event_id, content, timestamp) VALUES (?, ?, datetime('now'))",
                  (event_id, post_content))
        conn.commit()
        st.success("Post added successfully.")

    # Create Poll
    st.subheader("Create Poll")
    poll_question = st.text_input("Poll Question")
    poll_options = st.text_area("Poll Options (comma separated)")
    if st.button("Add Poll"):
        c.execute("INSERT INTO polls (event_id, question, options) VALUES (?, ?, ?)",
                  (event_id, poll_question, poll_options))
        conn.commit()
        st.success("Poll added successfully.")

    # Display Posts
    st.subheader("Event Posts")
    c.execute("SELECT content, timestamp FROM posts WHERE event_id = ?", (event_id,))
    posts = c.fetchall()
    for post in posts:
        st.write(post[0])
        st.caption(post[1])

    # Display Polls
    st.subheader("Event Polls")
    c.execute("SELECT question, options FROM polls WHERE event_id = ?", (event_id,))
    polls = c.fetchall()
    for poll in polls:
        st.write(poll[0])
        st.write("Options:", poll[1])

    conn.close()