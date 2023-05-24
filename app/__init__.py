from flask import Flask, render_template, request, session, redirect
from login import user_exist, create_user, confirm, get_pswd, correct_login
import sqlite3

app = Flask(__name__)
app.secret_key = "spinningchuckerswoah"

# connect to db
conn = sqlite3.connect('nycInfo.db')
cursor = conn.cursor()
# select from temperature table
cursor.execute('SELECT * from temperature')
temperature = cursor.fetchall()
temperature = [list(x) for x in temperature]
# select from health table
cursor.execute('SELECT * from health')
health = cursor.fetchall()
health = [list(x) for x in health]
# select from energy table
cursor.execute('SELECT * from energy')
energy = cursor.fetchall()
energy = [list(x) for x in energy]
# select from buildings table
cursor.execute('SELECT * from buildings')
buildings = cursor.fetchall()
buildings = [list(x) for x in buildings]
# select from transportation table
cursor.execute('SELECT * from transportation')
transportation = cursor.fetchall()
transportation = [list(x) for x in transportation]
# select from jobs table
cursor.execute('SELECT * from jobs')
jobs = cursor.fetchall()
jobs = [list(x) for x in jobs]
cursor.close()
conn.close()

# home page
@app.route("/home", methods = ["POST","GET"])
def root():
    return render_template('index.html', temperature = temperature)

@app.route("/", methods = ["POST","GET"])
def log():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['pswd']
        # checks if using is registered
        if (user_exist(username)):
            # checks if the entered username and password are correct
            if correct_login(username, password):
                session["username"] = username
                return redirect("/home")
            else:
                return render_template("login.html", message="Incorrect Password")
        else:
            return render_template("login.html", message="User not found")

@app.route("/register", methods = ["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form['register_username']
        password = request.form['register_pswd']
        same_pswd = request.form['pswd_confirm']
        # if the two entered passwords match, add the user info to the database
        if confirm(password, same_pswd):
            # if account if created, user directed to the home page
            if create_user(username, password):
                session["username"] = username
                return redirect("/home")
            elif user_exist(username):
                return render_template('register.html', message="Account creation failed. Username exists.")
            # if not, returns a message to tell the user to retry
            else:
                return render_template('register.html', message="Account creation failed. Please try again.")
        # if not, user stays on the register page
        else:
            return render_template('register.html',message="Passwords do not match.")
    #return render_template("login.html", message="An error occured")

@app.route("/logout", methods = ["POST","GET"])
def logout():
    session.pop('username', None)
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
