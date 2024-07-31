from datetime import datetime
from reserva_app.domain.model import Model
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala

class Reserva(Model):
    def __init__(self, sala: Sala, usuario: Usuario, inicio: datetime, fim: datetime, id: int = None, ativa: bool = True):
        self.id = id
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.ativa = ativa

    def to_row(self):
        return f"{self.id},{self.sala.id},{self.usuario.id},{self.inicio},{self.fim},{self.ativa}\n"