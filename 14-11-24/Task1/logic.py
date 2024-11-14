from db import Db

class Logic:
    def __init__(self):
        self.logic_db = Db()

    def add_user_logic(self, user):
        return self.logic_db.add_user(user)

    def get_all_user_logic(self):
        return self.logic_db.get_all_user()

    def clean_up_logic(self):
        return self.logic_db.clean_up()
