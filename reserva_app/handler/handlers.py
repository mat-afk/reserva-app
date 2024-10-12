from datetime import datetime
from reserva_app.util.constants import DEFAULT_DATETIME_FORMAT, DEFAULT_DATE_FORMAT
from reserva_app.domain.reserva import Reserva
from reserva_app.domain.sala import Sala, SalaType
from reserva_app.domain.error import Error
from reserva_app.dao.implementations import salaDAO, reservaDAO, usuarioDAO
from reserva_app.handler.auth_handlers import get_user_cookie

def get_salas():
    return salaDAO.find_all()

def get_salas_ativas():
    return salaDAO.find_all_ativas()

def get_sala_types():
    return SalaType

def get_sala_types_values():
    return [item.value for item in SalaType]

def get_reservas():
    return reservaDAO.find_all()

def get_reservas_for_today():
    return [reserva for reserva in get_reservas() if reserva.inicio.date() == datetime.today().date()]

def get_others_reservas():
    return [reserva for reserva in get_reservas() if reserva.inicio.date() != datetime.today().date()]


def get_reserva_by_id(id):
    return reservaDAO.find_by_id(int(id))

def filter_reservas(request):
    id = request.args.get("id", type = int)
    sala_id = request.args.get("sala", type = int)
    data = request.args.get("data")
    ativa = request.args.get("ativa", type = bool)

    if not id and not sala_id and not data and not ativa:
        return None
    
    reservas: list[Reserva] = get_reservas()
    
    filtered_reservas = []

    for reserva in reservas:
        if id and reserva.id != id:
            continue

        if sala_id and reserva.sala.id != sala_id:
            continue

        if data:
            reserva_date_str = reserva.inicio.strftime(DEFAULT_DATE_FORMAT)
            if reserva_date_str != data:
                continue

        if ativa:
            if reserva.ativa != ativa:
                continue

        filtered_reservas.append(reserva)

    return filtered_reservas

def handle_reservar_sala(request):
    sala_id = request.form["sala"]
    inicio = request.form["inicio"]
    fim = request.form["fim"]

    sala_id = int(sala_id)
    inputs = { "sala_id": sala_id, "inicio": inicio, "fim": fim }

    if not sala_id or not inicio or not fim:
        return [Error.BlankFields], inputs

    inicio = datetime.strptime(inicio, DEFAULT_DATETIME_FORMAT)
    fim = datetime.strptime(fim, DEFAULT_DATETIME_FORMAT)

    inputs["inicio"] = inicio
    inputs["fim"] = fim

    errors = validate_reservar_sala(inputs)

    if errors:
        return errors, inputs

    user_id = get_user_cookie()
    usuario = usuarioDAO.find_by_id(int(user_id))
    sala = salaDAO.find_by_id(int(sala_id))
    
    reserva = Reserva(sala, usuario, inicio, fim)

    reservaDAO.save(reserva)

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

    reservas: list[Reserva] = [reserva for reserva in reservaDAO.find_by_sala(sala_id) if reserva.ativa]

    for reserva in reservas:
        if reserva.inicio < fim and reserva.fim > inicio:
            reservaStart = reserva.inicio.time().strftime("%H:%M")
            reservaEnd = reserva.fim.time().strftime("%H:%M")
            return [str(Error.SalaAlreadyInUse) + f" Essa sala já foi reservada das {reservaStart} às {reservaEnd}."]
        
def handle_cancelar_reserva(id):
    id = int(id)
    reserva = reservaDAO.find_by_id(id)
    reserva.ativa = False
    reserva.id = id
    reservaDAO.update(reserva)
        
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

    sala = Sala(capacidade, tipo, descricao)

    salaDAO.save(sala)

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
    sala: Sala = salaDAO.find_by_id(id)
    sala.ativa = False
    sala.id = id
    salaDAO.update(sala)

def handle_excluir_sala(id: int):
    salaDAO.delete(id)
