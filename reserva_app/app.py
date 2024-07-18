from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="../templates")

loggedIn = False

@app.route("/")
def index():
    if not loggedIn:
        return redirect(url_for("login"))
        
    return redirect(url_for("reservas"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/reservas")
def reservas():
    return render_template("reservas.html")


@app.route("/salas")
def salas():
    return render_template("listar-salas.html")


@app.route("/salas/reservar")
def reservar_sala():
    return render_template("reservar-sala.html")

   
@app.route("/salas/cadastrar")
def cadastrar_sala():
    return render_template("cadastrar-sala.html")
