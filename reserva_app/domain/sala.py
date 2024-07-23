from enum import Enum
from reserva_app.domain.model import Model

class SalaType(Enum):
    LAB_INF = 1
    LAB_QUI = 2
    SALA_AULA = 3


class Sala(Model):
    def __init__(self, id, capacidade, ativa, tipo: SalaType, descricao):
        self.id = id
        self.capacidade = capacidade
        self.ativa = ativa
        self.tipo = tipo
        self.descricao = descricao

    def to_row(self):
        return f"{self.id},{self.capacidade},{self.ativa},{self.tipo},{self.descricao}\n"