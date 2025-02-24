def init_db():
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()

    # Create Events table
    c.execute('''CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    date TEXT,
                    time TEXT,
                    venue TEXT,
                    platform TEXT,
                    size INTEGER,
                    fee REAL,
                    is_paid BOOLEAN,
                    is_team_event BOOLEAN,
                    organizer_id INTEGER,
                    FOREIGN KEY (organizer_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()