from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def front_pg():
    return render_template('index.html')

@app.route("/indext.html")
def second_pg():
    return render_template('indext.html')

@app.route("/index3.html")
def third_pg():
    return render_template('index3.html')

@app.route("/index4.html")
def fourth_pg():
    return render_template('index4.html')