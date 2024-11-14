import sqlite3

# Connect to the SQLite database (it will create the database file if it doesn't exist)
connection = sqlite3.connect('my_poc_database.db')  # 'my_database.db' is the database file

#prove that you have got connection

# Create a cursor object to execute SQL commands
cursor = connection.cursor()




# Create a table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"User_name: {self.name}, age: {self.age}"

u1 = User("arun", 12)
# Insert a record into the table
insert_query = 'INSERT INTO users (name, age) VALUES (?, ?)'
cursor.execute(insert_query, (u1.name, u1.age))

# Commit the transaction to save changes to the database
connection.commit()

# Query to retrieve all records from the users table
cursor.execute('SELECT * FROM users')

# Fetch all rows from the executed query
rows = cursor.fetchall()

user_list = []

for row in rows:
    user_list.append(User(row[1], row[2]))

# Print the data
print("Data in users table:")
for row in user_list:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
"""
 3 files
  user.py
  db.py -> 
    insert(user obj) ret Bool
    get_all() -> all the rows
    clean_up closes data corsor
    
  logic.py -> call and return
    insert_logice
    get_all
    clean_up

"""