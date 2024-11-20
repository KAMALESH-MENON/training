from user import User
from logic import Logic
from db import Db
if __name__ == "__main__":
    l1 = Logic()
    u1 = User(1, "John", 43)
    u2 = User(2, "Rahul", 38)
    u3 = User(3, "Bhaskar", 45)
    u4 = User(4, "Vasu", 35)

    db1 = Db()
    USER_ADD_RESULT = db1.add_user(u3)
    print(USER_ADD_RESULT)

    # USERS = db1.get_all_user()
    # for user in USERS:
    #     print(user)

    # CLEANUP_RESULT = db1.clean_up()
    # print(CLEANUP_RESULT)

    # print(l1.get_all_user_logic())

    # for i in l1.get_all_user_logic():
    #     print(i)
    #print(l1.clean_up_logic())