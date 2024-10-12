from enum import Enum
from reserva_app.domain.model import Model

class SalaType(Enum):
    LAB_INF = 1
    LAB_QUI = 2
    SALA_AULA = 3

    def __str__(self):
        return {
            SalaType.LAB_INF: "Laboratório de Informática",
            SalaType.LAB_QUI: "Laboratório de Química",
            SalaType.SALA_AULA: "Sala de Aula"
        }[self]


class Sala(Model):
    def __init__(self, capacidade: int, tipo: SalaType, descricao: str, id: int = None, ativa: bool = True):
        self.id = id
        self.capacidade = capacidade
        self.ativa = ativa
        self.tipo = tipo
        self.descricao = descricao

    def to_row(self):
        return f"{self.id},{self.capacidade},{self.ativa},{self.tipo.value},{self.descricao}\n"
    
    def __str__(self):
        atts = []
        for key, value in self.__dict__.items():
            atts.append(f"{key}={value}")
        return f"{__class__.__name__}: {", ".join(atts)}\n"