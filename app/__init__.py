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
#     # work in progress
#
# @app.route("/logout", methods = ["POST"])
# def logout():
#     session.pop('username', None)
#     return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()