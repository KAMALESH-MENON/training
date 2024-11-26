import sqlite3

def db_connection():
    """
    connects to database and returns cursor.
    """
    connection = sqlite3.connect('POC_Test.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS employee 
                   ( emp_no INTEGER PRIMARY KEY, 
                   emp_name TEXT NOT NULL, 
                   location TEXT NOT NULL, 
                   dept_id INTEGER NOT NULL ) ''')
    return cursor

if __name__ == "__main__":
    db_connection()
