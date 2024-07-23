from datetime import datetime

class Reserva:
    def __init__(self, id, usuario_id, sala_id, inicio: datetime, fim: datetime, ativo):
        self.id = id
        self.usuario_id = usuario_id
        self.sala_id = sala_id
        self.inicio = inicio
        self.fim = fim
        self.ativo = ativo

    def to_row(self):
        return f"{self.id},{self.usuario_id},{self.sala_id},{self.inicio},{self.fim},{self.ativo}"