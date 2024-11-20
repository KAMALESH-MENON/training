import sqlite3

DATABASE_FILE = 'PS2-DB.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        product_ids TEXT NOT NULL,
        total REAL NOT NULL
    )
    ''')
    return conn
