import sqlite3
from pathlib import Path

DB_PATH = Path("vartex.db")

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    with conn() as c:
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT,
            credits INTEGER NOT NULL DEFAULT 0, joined_at TEXT DEFAULT CURRENT_TIMESTAMP
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL,
            action TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )''')

def register(user):
    with conn() as c:
        c.execute("INSERT OR IGNORE INTO users(user_id,username,first_name) VALUES(?,?,?)",
                  (user.id, user.username or "", user.first_name or ""))
        c.execute("UPDATE users SET username=?,first_name=? WHERE user_id=?",
                  (user.username or "", user.first_name or "", user.id))

def get_user(uid):
    with conn() as c:
        return c.execute("SELECT * FROM users WHERE user_id=?", (uid,)).fetchone()

def log(uid, action):
    with conn() as c:
        c.execute("INSERT INTO activity(user_id,action) VALUES(?,?)", (uid, action))

def history(uid):
    with conn() as c:
        return c.execute("SELECT action,created_at FROM activity WHERE user_id=? ORDER BY id DESC LIMIT 8", (uid,)).fetchall()

def user_count():
    with conn() as c:
        return c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
