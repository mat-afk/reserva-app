from flask import Flask, render_template, redirect, url_for, request
from reserva_app.handler.auth_handlers import handle_login, handle_cadastro
from reserva_app.handler.sala_handlers import get_salas, get_sala_types, handle_cadastrar_sala, handle_desativar_sala, handle_excluir_sala

app = Flask(__name__, template_folder="../templates")

loggedIn = False

@app.route("/")
def index():
    if not loggedIn:
        return redirect(url_for("login"))
        
    return redirect(url_for("reservas"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", inputs={})
    
    if request.method == "POST":
        errors, inputs = handle_login(request)

        if errors:
            return render_template("login.html", errors=errors, inputs=inputs)

        return redirect(url_for("reservas"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html", inputs={})
    
    if request.method == "POST":
        errors, inputs = handle_cadastro(request)

        if errors:
            return render_template("cadastro.html", errors=errors, inputs=inputs)

        return redirect(url_for("reservas"))


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
        return render_template("cadastrar-sala.html", tipos=get_sala_types(), inputs={})
    
    if request.method == "POST":
        errors, inputs = handle_cadastrar_sala(request)

        if errors:
            return render_template("cadastrar-sala.html", tipos=get_sala_types(), errors=errors, inputs=inputs)
        
        return redirect(url_for("salas"))
    

@app.route("/salas/<id>/desativar", methods=["POST"])
def desativar_sala(id):
    handle_desativar_sala(int(id))
    return redirect(url_for("salas"))


@app.route("/salas/<id>/excluir", methods=["POST"])
def excluir_sala(id):
    handle_excluir_sala(int(id))
    return redirect(url_for("salas"))