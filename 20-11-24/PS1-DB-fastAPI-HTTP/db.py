import sqlite3

DATABASE_FILE = 'products.db'

def db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')
    return conn
