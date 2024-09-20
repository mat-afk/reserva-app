from datetime import datetime
from reserva_app.repository.repository import Repository
from reserva_app.domain.model import Model
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala, SalaType
from reserva_app.domain.reserva import Reserva
from reserva_app.util.constants import DATETIME_FORMAT

class UsuarioRepository(Repository):

    FILE_NAME = "usuarios.csv"

    def __init__(self):
        super().__init__(self.FILE_NAME)

    def find_by_email(self, email:str) -> Model:
        for model in self.find_all():
            if model.email == email:
                return model
            
        return None

    def convert_to_model(self, row: str) -> Model:
        id, nome, email, senha, ativo, admin = row.strip().split(",")

        id = int(id)
        ativo = self.str_to_bool(ativo)
        admin = self.str_to_bool(admin)

        return Usuario(nome, email, senha, id=id, ativo=ativo, admin=admin)


class SalaRepository(Repository):

    FILE_NAME = "salas.csv"
    ID_OFFSET = 100

    def __init__(self):
        super().__init__(self.FILE_NAME)

    def convert_to_model(self, row: str) -> Model:
        id, capacidade, ativa, tipo, descricao = self.split_fields(row)

        capacidade = int(capacidade)
        tipo = SalaType(int(tipo))
        id = int(id)
        ativa = self.str_to_bool(ativa)
        
        return Sala(capacidade, tipo, descricao, id=id, ativa=ativa)
    

class ReservaRepository(Repository):

    FILE_NAME = "reservas.csv"

    def __init__(self):
        super().__init__(self.FILE_NAME)

    def find_by_sala(self, sala_id: int) -> list[Model]:
        return [model for model in self.find_all() if model.sala.id == sala_id]

    def convert_to_model(self, row: str) -> Model:
        id, sala_id, usuario_id, inicio, fim, ativa = row.strip().split(",")

        id = int(id)
        sala = salaRepository.find_by_id(int(sala_id))
        usuario = usuarioRepositoy.find_by_id(int(usuario_id))
        inicio = datetime.strptime(inicio, DATETIME_FORMAT)
        fim = datetime.strptime(fim, DATETIME_FORMAT)
        ativa = self.str_to_bool(ativa)
        
        return Reserva(sala, usuario, inicio, fim, id=id, ativa=ativa)


usuarioRepositoy = UsuarioRepository()

salaRepository = SalaRepository()

reservaRepository = ReservaRepository()