from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

# home page
@app.route("/")
def root():
    return render_template('index.html')

# @app.route("/")
# def login():
#     username = request.form['username']
#     password = request.form['pswd']
#     if (user_exist(username)):
#         if correct_login(username, password):
#             session["username"] = username
#             return redirect("/home")
#         else:
#             return render_template("login.html", message="Incorrect Password")
#     else:
#         return render_template("login.html", message="User not found")
#
# @app.route("/register")
# def register():
#     username = request.form['register_username']
#     password = request.form['register_pswd']
#     same_pswd = request.form['pswd_confirm']
#     # if the two entered passwords match, add the user info to the database
#     if confirm(password, same_pswd):
#         # if account if created, user directed to the home page
#         if create_user(username, password):
#             session["username"] = username
#             return redirect("/home")
#         # if not, returns a message to tell the user to retry
#         else:
#             return render_template('register.html', message="Account creation failed. Please try again.")
#     # if not, user stays on the register page
#     return render_template('register.html',message="Passwords do not match.")

#
# @app.route("/logout", methods = ["POST"])
# def logout():
#     session.pop('username', None)
#     return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()