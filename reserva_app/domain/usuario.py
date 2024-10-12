from reserva_app.domain.model import Model

class Usuario(Model):
    def __init__(self, nome: str, email: str, senha: str, id: int = None, ativo: bool = True, admin: bool = False):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__ativo = ativo
        self.__admin = admin

    def to_row(self):
        return f"{self.__id},{self.__nome},{self.__email},{self.__senha},{self.__ativo},{self.__admin}\n"

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo: bool):
        self.__ativo = ativo

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, admin: bool):
        self.__admin = admin

    def __str__(self):
        return f"Usuario (id={self.__id}, nome={self.__nome}, email={self.__email}, senha={self.__senha}, ativo={self.__ativo}, admin={self.__admin})"