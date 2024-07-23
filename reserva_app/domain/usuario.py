from reserva_app.domain.model import Model

class Usuario(Model):
    def __init__(self, nome, email, senha, ativo, admin):
        self.id = 0
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

    def to_row(self):
        return f"{self.id},{self.nome},{self.email},{self.senha},{self.ativo},{self.admin}\n"
