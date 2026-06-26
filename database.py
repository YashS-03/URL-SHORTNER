import sqlite3

def init_db():
    conn = sqlite3.connect("urls.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS urls(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT,
        short_code TEXT,
        clicks INTEGER
    )
    """)

    conn.commit()
    conn.close()

def save_url(original_url, short_code):
    conn = sqlite3.connect("urls.db")
    cur  = conn.cursor()

    cur.execute("INSERT INTO urls (original_url, short_code, clicks) VALUES (?,?,?)",
                (original_url, short_code, 0))
    conn.commit()
    conn.close()

def get_url(short_code):
    conn = sqlite3.connect("urls.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM urls WHERE short_code = ?",(short_code,))
    result = cur.fetchone()
    conn.close()
    return result

