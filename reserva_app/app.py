from flask import Flask, render_template, redirect, url_for, request
from reserva_app.handler.handlers import get_salas, get_sala_types, handle_cadastrar_sala

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


@app.route("/reservas/<id>")
def detalhes_reserva():
    return render_template("reserva/detalhes-reserva.html")


@app.route("/salas")
def salas():
    return render_template("listar-salas.html", salas=get_salas())


@app.route("/salas/reservar")
def reservar_sala():
    return render_template("reservar-sala.html")


@app.route("/salas/cadastrar", methods=["GET", "POST"])
def cadastrar_sala():
    if request.method == "GET":
        return render_template("cadastrar-sala.html", tipos=get_sala_types())
    
    if request.method == "POST":
        handle_cadastrar_sala(request)
        return redirect(url_for("salas"))