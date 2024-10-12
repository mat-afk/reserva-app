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
        self.__id = id
        self.__capacidade = capacidade
        self.__ativa = ativa
        self.__tipo = tipo
        self.__descricao = descricao

    def to_row(self):
        return f"{self.__id},{self.__capacidade},{self.__ativa},{self.__tipo.value},{self.__descricao.replace(',', ' ')}\n"
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, ativa: bool):
        self.__ativa = ativa

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: SalaType):
        self.__tipo = tipo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    def __str__(self):
        return f"Sala (id={self.__id}, capacidade={self.__capacidade}, ativa={self.__ativa}, tipo={self.__tipo}, descricao={self.__descricao})"