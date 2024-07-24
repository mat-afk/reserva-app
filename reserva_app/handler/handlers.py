from reserva_app.domain.sala import Sala, SalaType
from reserva_app.repository.repository import salaRepository

def get_salas():
    return salaRepository.list()

def get_sala_types():
    return SalaType

def handle_cadastrar_sala(request):
    tipo = request.form["tipo"]
    capacidade = request.form["capacidade"]
    descricao = request.form["descricao"]

    sala = Sala(capacidade, SalaType(int(tipo)), descricao)

    salaRepository.save(sala)