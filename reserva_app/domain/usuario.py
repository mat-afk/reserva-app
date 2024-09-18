from reserva_app.domain.model import Model

class Usuario(Model):
    def __init__(self, nome: str, email: str, senha: str, id: int = None, ativo: bool = True, admin: bool = False):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

    def to_row(self):
        return f"{self.id},{self.nome},{self.email},{self.senha},{self.ativo},{self.admin}\n"

    def __str__(self):
        return f"{self.id},{self.nome},{self.email},{self.senha},{self.ativo},{self.admin}\n"