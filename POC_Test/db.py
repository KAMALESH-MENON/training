import sqlite3

def db_connection():
    connection = sqlite3.connect('POC_Test.db', check_same_thread=False)
    cursor = connection.cursor()
    return cursor

if __name__ == "__main__":
    db_connection()
