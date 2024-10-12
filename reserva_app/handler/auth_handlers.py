import bcrypt
import re
from flask import session
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.error import Error
from reserva_app.util.constants import PASSWORD_MIN_LENGHT
from reserva_app.dao.implementations import usuarioDAO

def get_user_cookie():
    return session.get("auth_user")

def set_user_cookie(id):
    session["auth_user"] = id

def pop_user_cookie():
    session.pop("auth_user")

def handle_login(request):
    email = request.form["email"]
    senha = request.form["password"]

    inputs = { "email": email, "senha": senha }

    usuario = usuarioDAO.find_by_email(email)

    errors = validate_login(inputs, usuario)
    if errors:
        return errors, inputs
    
    set_user_cookie(usuario.id)

    return None, None

def validate_login(inputs, usuario):
    email = inputs["email"]
    senha = inputs["senha"]

    if not email or not senha:
        return [Error.BlankFields]
    
    if not is_email_valid(email):
        return [Error.InvalidEmail]

    if not usuario or not check(senha, usuario.senha):
        return [Error.BadCredentials]

    return None

def handle_cadastro(request):
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["password"]

    inputs = { "nome": nome, "email": email, "senha": senha }

    errors = validate_cadastro(inputs)

    if errors:
        return errors, inputs
    
    senha = hash(senha)

    usuario = Usuario(nome, email, senha)

    user_id = usuarioDAO.save(usuario)

    set_user_cookie(user_id)

    return None, None

def validate_cadastro(inputs):
    nome = inputs["nome"]
    email = inputs["email"]
    senha =  inputs["senha"]

    errors = []

    if not nome or not email or not senha:
        return [Error.BlankFields]

    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9 ]+$", nome):
        errors.append(Error.NameSpecialCharacters)
    
    if not is_email_valid(email):
        errors.append(Error.InvalidEmail)

    if len(senha) < PASSWORD_MIN_LENGHT:
        errors.append(Error.PasswordMinimumLength)

    if usuarioDAO.find_by_email(email):
        errors.append(Error.UnavailableEmail)

    return errors

def hash(senha: str):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

def check(senha: str, hashed: str):
    return bcrypt.checkpw(senha.encode(), hashed.encode())

def is_email_valid(email):
    return re.match(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$", email)
