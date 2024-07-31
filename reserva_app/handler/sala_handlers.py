from datetime import datetime
from reserva_app.domain.reserva import Reserva
from reserva_app.domain.sala import Sala, SalaType
from reserva_app.domain.error import Error
from reserva_app.repository.repository import salaRepository, reservaRepository, usuarioRepositoy
from reserva_app.handler.auth_handlers import get_user_cookie

def get_salas():
    return salaRepository.find_all()

def get_sala_types():
    return SalaType

def get_sala_types_values():
    return [item.value for item in SalaType]

def handle_reservar_sala(request):
    sala_id = request.form["sala"]
    inicio = request.form["inicio"]
    fim = request.form["fim"]

    sala_id = int(sala_id)
    inputs = { "sala_id": sala_id, "inicio": inicio, "fim": fim }

    if not sala_id or not inicio or not fim:
        return [Error.BlankFields], inputs

    inicio = datetime.strptime(inicio, "%Y-%m-%dT%H:%M")
    fim = datetime.strptime(fim, "%Y-%m-%dT%H:%M")

    inputs["inicio"] = inicio
    inputs["fim"] = fim

    errors = validate_reservar_sala(inputs)

    if errors:
        return errors, inputs

    user_id = get_user_cookie()
    usuario = usuarioRepositoy.find_by_id(user_id)
    sala = salaRepository.find_by_id(sala_id)
    
    reserva = Reserva(sala, usuario, inicio, fim)

    reservaRepository.save(reserva)

    return None, None

def validate_reservar_sala(inputs):
    sala_id = inputs["sala_id"]
    inicio = inputs["inicio"]
    fim = inputs["fim"]

    errors = []

    now = datetime.now()

    if inicio < now:
        errors.append(Error.InvalidReservaStartDate)

    if fim < now:
        errors.append(Error.InvalidReservaEndDate)

    if errors:
        return errors

    if fim <= inicio:
        return [Error.ReservaEndBeforeStart]

    if fim.date() > inicio.date():
        return [Error.ReservaTooLong]

    reservas: list[Reserva] = reservaRepository.find_by_sala(sala_id)

    for reserva in reservas:
        if reserva.inicio < fim and reserva.fim > inicio:
            reservaStart = reserva.inicio.time().strftime("%H:%M")
            reservaEnd = reserva.fim.time().strftime("%H:%M")
            return [str(Error.SalaAlreadyInUse) + f" Essa sala já foi reservada das {reservaStart} às {reservaEnd}."]
        
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
        return [Error.BlankFields]
    
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
