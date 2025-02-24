import sqlite3

def add_sample_events():
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()

    # Sample events data
    sample_events = [
        ("Python Workshop", "Learn Python programming.", "2023-10-15", "10:00:00", "Online", "Zoom", 50, 0.0, True, False, 1),
        ("Data Science Seminar", "Explore data science concepts.", "2023-10-20", "14:00:00", "Conference Room A", "In-Person", 100, 20.0, True, True, 1),
        ("Web Development Bootcamp", "Build websites from scratch.", "2023-11-01", "09:00:00", "Online", "Google Meet", 30, 0.0, True, False, 1),
    ]

    # Insert sample events into the events table
    c.executemany("INSERT INTO events (title, description, date, time, venue, platform, size, fee, is_paid, is_team_event, organizer_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", sample_events)

    conn.commit()
    conn.close()
    print("Sample events added successfully.")

if __name__ == "__main__":
    add_sample_events()