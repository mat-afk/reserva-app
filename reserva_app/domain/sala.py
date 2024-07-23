from enum import Enum

class SalaType(Enum):
    LAB_INF = "Laboratório de Informática"
    LAB_QUI = "Laboratório de Química"
    SALA_AULA = "Sala de Aula"


class Sala:
    def __init__(self, capacidade, ativa, tipo: SalaType, descricao):
        self.id = 0
        self.capacidade = capacidade
        self.ativa = ativa
        self.tipo = tipo
        self.descricao = descricao

    def to_row(self):
        return f"{self.id},{self.capacidade},{self.ativa},{self.tipo},{self.descricao}"