import bcrypt
import re

from reserva_app.domain.usuario import Usuario
from reserva_app.domain.error import Error
from reserva_app.domain.constants import PASSWORD_MIN_LENGHT
from reserva_app.repository.repository import usuarioRepositoy

def handle_login(request):
    email = request.form["email"]
    senha = request.form["password"]

    inputs = { "email": email, "senha": senha }

    errors = validate_login(inputs)

    if errors:
        return errors, inputs

    return None, None

def validate_login(inputs):
    email = inputs["email"]
    senha = inputs["senha"]

    if not email or not senha:
        return [Error.BlankCredentials]
    
    if not is_email_valid(email):
        return [Error.InvalidEmail]

    usuario = usuarioRepositoy.find_by_email(email)
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

    usuarioRepositoy.save(usuario)

    return None, None

def validate_cadastro(inputs):
    nome = inputs["nome"]
    email = inputs["email"]
    senha =  inputs["senha"]

    errors = []

    if not nome or not email or not senha:
        return [Error.BlankCredentials]

    if re.match(r".*[^a-zA-Z0-9].*", nome):
        errors.append(Error.NameSpecialCharacters)
    
    if not is_email_valid(email):
        errors.append(Error.InvalidEmail)

    if len(senha) < PASSWORD_MIN_LENGHT:
        errors.append(Error.PasswordMinimumLength)

    if usuarioRepositoy.find_by_email(email):
        errors.append(Error.UnavailableEmail)

    return errors

def hash(senha: str):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

def check(senha: str, hashed: str):
    return bcrypt.checkpw(senha.encode(), hashed.encode())

def is_email_valid(email):
    return re.match(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$", email)
