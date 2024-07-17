from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="../templates")

loggedIn = False

#Cadastrar sala e listar sala
def register_sala(tipo, capacidade, descricao):
    self.tipo = tipo
    self.capacidade = capacidade
    self.descricao = descricao


def list_salas()
    sala_list[] = 

@app.route("/")
def index():
    if not loggedIn:
        return redirect(url_for("login"))
        
    return redirect(url_for("salas"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def home():
    return render_template("cadastro.html")

@app.route("/reservas")
def home():
    return render_template("reserva/detalhes-reserva.html")

@app.route("/reservas/reservar")
def home():
    return render_template("reservar-sala.html")

@app.route("/salas")
def home():
    return render_template("listar-salas.html")
    
@app.route("/salas/cadastro")
def home():
    return render_template("cadastrar-sala.html")
    
