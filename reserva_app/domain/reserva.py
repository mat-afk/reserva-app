from datetime import datetime
from reserva_app.domain.model import Model
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala
from reserva_app.util.constants import DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT

class Reserva(Model):
    def __init__(self, sala: Sala, usuario: Usuario, inicio: datetime, fim: datetime, id: int = None, ativa: bool = True):
        self.id = id
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.ativa = ativa

    def date(self):
        return self.inicio.date().strftime(DATE_FORMAT)
    
    def time_inicio(self):
        return self.inicio.time().strftime(TIME_FORMAT)
    
    def time_fim(self):
        return self.fim.time().strftime(TIME_FORMAT)

    def formatted_inicio(self):
        return self.inicio.strftime(DATETIME_FORMAT)
    
    def formatted_fim(self):
        return self.fim.strftime(DATETIME_FORMAT)

    def to_row(self):
        return f"{self.id},{self.sala.id},{self.usuario.id},{self.formatted_inicio()},{self.formatted_fim()},{self.ativa}\n"
    
    def __str__(self):
        return f"{self.id},{self.sala},{self.usuario},{self.inicio},{self.fim},{self.ativa}\n"