# helper file for login and register

import sqlite3

DB_FILE = "user.ub"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, pass TEXT)")

# check if the username is in the database
# returns True if username exists, False otherwise
def user_exist(username):
    g = list(c.execute("SELECT name from users").fetchall())
    for i in g:
        for j in i:
            if username == j:
                return True
    return False

# creates an account
# returns True if account is created, False otherwise
def create_user(username, password):
    # if username or password is blank
    if (username == "") or (password == ""):
        return False
    # if username already exists
    if user_exist(username):
        return False
    # create user
    c.execute("INSERT INTO users VALUES(?,?)", (username, password))
    db.commit()
    return True

# when registering, make sure that the passwords entered match
# returns True if passwords match, False otherwise
def confirm(password, pswd_confirm):
    return password == pswd_confirm

# gets the password from the corresponding username (for the login page)
# returns False if username does not exist (so we can't get the corresponding password)
def get_pswd(username):
    if user_exist(username):
        g = list(c.execute("SELECT * FROM users").fetchall())
        for i in g:
            if i[0] == username:
                return i[1]
    return False

# makes sure that the password entered on the login page is correct
def correct_login(password):
    # work in progress
    return False