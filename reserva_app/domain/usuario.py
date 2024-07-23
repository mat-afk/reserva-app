class Usuario:
    def __init__(self, id, nome, email, senha, ativo, admin):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

    def to_row(self):
        return f"{self.id},{self.nome},{self.email},{self.senha},{self.ativo},{self.admin}"
