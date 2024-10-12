from datetime import datetime
from reserva_app.domain.model import Model
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala
from reserva_app.util.constants import DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT

class Reserva(Model):
    def __init__(self, sala: Sala, usuario: Usuario, inicio: datetime, fim: datetime, id: int = None, ativa: bool = True):
        self.__id = id
        self.__sala = sala
        self.__usuario = usuario
        self.__inicio = inicio
        self.__fim = fim
        self.__ativa = ativa

    def date(self):
        return self.__inicio.date().strftime(DATE_FORMAT)
    
    def time_inicio(self):
        return self.__inicio.time().strftime(TIME_FORMAT)
    
    def time_fim(self):
        return self.__fim.time().strftime(TIME_FORMAT)

    def formatted_inicio(self):
        return self.__inicio.strftime(DATETIME_FORMAT)
    
    def formatted_fim(self):
        return self.__fim.strftime(DATETIME_FORMAT)

    def to_row(self):
        return f"{self.__id},{self.__sala.id},{self.__usuario.id},{self.formatted_inicio()},{self.formatted_fim()},{self.__ativa}\n"
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, sala: Sala):
        self.__sala = sala

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: Usuario):
        self.__usuario = usuario

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio: datetime):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim: datetime):
        self.__fim = fim

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, ativa: bool):
        self.__ativa = ativa

    def __str__(self):
        return f"Reserva (id={self.__id}, sala={self.__sala}, usuario={self.__usuario}, inicio={self.formatted_inicio()}, fim={self.formatted_fim()}, ativa={self.__ativa})"