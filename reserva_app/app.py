from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="../templates")

loggedIn = False

@app.route("/")
def index():
    if not loggedIn:
        return redirect(url_for("login"))
    
    return render_template("reservas.html")

@app.route("/login")
def login():
    return render_template("login.html")