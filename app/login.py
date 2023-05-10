import sqlite3

DB_FILE = "user.ub"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS usernames(user TEXT, pass TEXT)")

# check if the username is in the database
def user_exist(username):
    g = list(c.execute("SELECT user from usernames").fetchall())
    for i in username_list:
        for j in i:
            if username == j:
                return True
    return False

# creates an account
def create_user(username, password):
