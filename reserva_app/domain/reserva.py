from datetime import datetime
from reserva_app.domain.model import Model

class Reserva(Model):
    def __init__(self, usuario_id: int, sala_id: int, inicio: datetime, fim: datetime, id: int = None, ativo: bool = True):
        self.id = id
        self.usuario_id = usuario_id
        self.sala_id = sala_id
        self.inicio = inicio
        self.fim = fim
        self.ativo = ativo

    def to_row(self):
        return f"{self.id},{self.usuario_id},{self.sala_id},{self.inicio},{self.fim},{self.ativo}\n"