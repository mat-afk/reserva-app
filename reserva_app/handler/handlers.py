from reserva_app.domain.sala import Sala, SalaType
from reserva_app.repository.repository import salaRepository

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

    errors = []

    if not tipo or not capacidade:
        return ["Por favor, preencha todos os campos obrigatórios."]
    
    if tipo not in str(get_sala_types_values()):
        errors.append("Selecione um tipo válido.")
    
    capacidade = int(capacidade)
    if capacidade <= 0:
        errors.append("A capacidade deve ser maior que 0.")

    if errors:
        return errors
    
    tipo = SalaType(int(tipo))
    descricao = '"' + descricao + '"'

    sala = Sala(capacidade, tipo, descricao)

    salaRepository.save(sala)