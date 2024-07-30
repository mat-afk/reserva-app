from reserva_app.domain.sala import Sala, SalaType
from reserva_app.domain.error import Error
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
        return [Error.BlankCredentials]
    
    if tipo not in str(get_sala_types_values()):
        errors.append(Error.InvalidSalaType)
    
    capacidade = int(capacidade)
    if capacidade <= 0:
        errors.append(Error.ZeroCapacity)

    return errors

def handle_desativar_sala(id: int):
    sala: Sala = salaRepository.find_by_id(id)
    sala.ativa = False
    salaRepository.update(id, sala)

def handle_excluir_sala(id: int):
    salaRepository.delete(id)
