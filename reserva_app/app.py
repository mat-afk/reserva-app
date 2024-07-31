from flask import Flask, render_template, redirect, url_for, request
from reserva_app.handler.auth_handlers import handle_login, handle_cadastro, get_user_cookie, pop_user_cookie
from reserva_app.handler.handlers import *

app = Flask(__name__, template_folder="../templates")
app.secret_key = "secret_key"

def redirect_logged_in():
    if not get_user_cookie():
        return redirect(url_for("login"))
    return None

@app.route("/")
def index():
    response = redirect_logged_in()
    if response:
        return response

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
    

@app.route("/logout", methods=["POST"])
def logout():
    pop_user_cookie()
    return redirect("/")


@app.route("/reservas")
def reservas():
    response = redirect_logged_in()
    if response:
        return response
    
    if not request.args:
        return render_template("reservas.html", reservas=get_reservas())
    
    filtered_reservas = filter_reservas(request)
    return render_template("reservas.html", reservas=filtered_reservas)


@app.route("/reservas/<id>")
def detalhes_reserva(id):
    reserva = get_reserva_by_id(id)
    return render_template("reserva/detalhes-reserva.html", reserva=reserva)


@app.route("/reservas/<id>/cancelar", methods=["POST"])
def cancelar_reserva(id):
    handle_cancelar_reserva(id)
    return redirect(url_for("reservas"))


@app.route("/salas")
def salas():
    response = redirect_logged_in()
    if response:
        return response
    
    return render_template("listar-salas.html", salas=get_salas())


@app.route("/salas/reservar", methods=["GET", "POST"])
def reservar_sala():
    response = redirect_logged_in()
    if response:
        return response
    
    salas = get_salas_ativas()

    if request.method == "GET":
        return render_template("reservar-sala.html", salas=salas, inputs={})
    
    if request.method == "POST":
        errors, inputs = handle_reservar_sala(request)

        if errors:
            return render_template("reservar-sala.html", salas=salas, inputs=inputs, errors=errors)

        return redirect(url_for("reservas"))


@app.route("/salas/cadastrar", methods=["GET", "POST"])
def cadastrar_sala():
    response = redirect_logged_in()
    if response:
        return response
    
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