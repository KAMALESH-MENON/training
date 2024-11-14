class User:
    def __init__(self, user_id, name, age):
        self.user_id = 0
        self.name = name
        self.age = age
    def __str__(self):
        return f"Username: {self.name}, age: {self.age}"