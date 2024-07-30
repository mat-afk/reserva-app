import bcrypt
import re

from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala, SalaType
from reserva_app.repository.repository import salaRepository, usuarioRepositoy

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
        return ["Por favor, preencha todos os campos."]
    
    if not is_email_valid(email):
        return ["Insira um e-mail válido."]

    usuario = usuarioRepositoy.find_by_email(email)
    if not usuario or not check(senha, usuario.senha):
        return ["E-mail ou senha incorretos."]

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
        return ["Por favor, preencha todos os campos obrigatórios."]

    if re.match(r".*[^a-zA-Z0-9].*", nome):
        errors.append("O nome não pode ter caracteres especiais.")
    
    if not is_email_valid(email):
        errors.append("Insira um e-mail válido.")

    MIN_LENGHT = 6
    if len(senha) < MIN_LENGHT:
        errors.append(f"A senha deve ter, no mínimo, {MIN_LENGHT} caracteres.")

    if usuarioRepositoy.find_by_email(email):
        errors.append("Email indisponível.")

    return errors

def hash(senha: str):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

def check(senha: str, hashed: str):
    return bcrypt.checkpw(senha.encode(), hashed.encode())

def is_email_valid(email):
    return re.match(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$", email)

def get_salas():
    return salaRepository.find_all()

def get_sala_types():
    return SalaType

def get_sala_types_values():
    return [item.value for item in SalaType]

def handle_cadastrar_sala(request):
    tipo = request.form["tipo"]
    capacidade = request.form["capacidade"]
    descricao = request.form["descricao"]

    inputs = { "tipo": tipo, "capacidade": capacidade, "descricao": descricao }

    errors = validate_cadastrar_sala(inputs)

    if errors:
        inputs["tipo"] = int(tipo)
        return errors, inputs
    
    tipo = SalaType(int(tipo))
    descricao = '"' + descricao + '"'

    sala = Sala(capacidade, tipo, descricao)

    salaRepository.save(sala)

    return None, None

def validate_cadastrar_sala(inputs):
    tipo = inputs["tipo"]
    capacidade = inputs["capacidade"]

    errors = []

    if not tipo or not capacidade:
        return ["Por favor, preencha todos os campos obrigatórios."]
    
    if tipo not in str(get_sala_types_values()):
        errors.append("Selecione um tipo válido.")
    
    capacidade = int(capacidade)
    if capacidade <= 0:
        errors.append("A capacidade deve ser maior que 0.")

    return errors

def handle_desativar_sala(id: int):
    sala: Sala = salaRepository.find_by_id(id)
    sala.ativa = False
    salaRepository.update(id, sala)

def handle_excluir_sala(id: int):
    salaRepository.delete(id)
