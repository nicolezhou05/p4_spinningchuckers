from flask import Flask, render_template
app = Flask(__name__)

# home page
@app.route("/")
def root():
    return render_template('home.html')

# crime rates page
@app.route("/crimerates")
def crimepage():
    return render_template('crime.html')

# environment tracker page (weather/climate)
@app.route("/environment")
def environment():
    return render_template('env.html')

# transportation page
@app.route("/transportation")
def transportion():
    return render_template('trans.html')

# energy page
@app.route("/energy")
def energy():
    return render_template('energy.html')

# job market page
@app.route("/job")
def crimepage():
    return render_template('job.html')

if __name__ == "__main__":
    app.debug = True
    app.run()