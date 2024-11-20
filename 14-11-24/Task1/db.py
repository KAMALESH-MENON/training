import sqlite3
from user import User

class Db:
    def __init__(self):
        self.connection = sqlite3.connect('Task1_database.db') 
        self.cursor = self.connection.cursor()

    def add_user(self, user):
        added_result = False
        try:
            insert_query = 'INSERT INTO users (name, age) VALUES (?, ?)'
            self.cursor.execute(insert_query, (user.name, user.age))
            self.connection.commit()
            added_result = True
        except IntegrityError as e:
            print(f"Error: {e}")
        finally:
            return added_result

    def get_all_user(self):
        user_list = []
        try:
            self.cursor.execute('SELECT * FROM users')
            rows = self.cursor.fetchall()
            for row in rows:
                user_list.append(row[0], row[1], row[2])
        finally:
            return user_list

    def clean_up(self):
        result = False
        try:
            self.cursor.close()
            self.connection.close()
            result = True
        finally:
            return result