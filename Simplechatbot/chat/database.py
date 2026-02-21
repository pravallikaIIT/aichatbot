import sqlite3

DB_NAME = "chat.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            sender TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()