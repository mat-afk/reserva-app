from reserva_app.domain.sala import Sala
from reserva_app.domain.model import Model
from pathlib import Path

class Repository:

    DATABASE_PATH = Path(__file__).parents[2] / "database/"
    ID_OFFSET = 1

    def __init__(self, source_path):
        self.file_path = self.DATABASE_PATH / source_path

    def list(self):
        with open(self.file_path) as file:
            return [self.convert_to_model(row) for row in file]

    def save(self, model: Model):
        with open(self.file_path, "a") as file:
            model.id = self.new_id()
            row = model.to_row()
            file.write(row)

    def find_by_id(self, id: int):
        for model in self.list():
            if model.id == id:
                return model

    def convert_to_model(self, row: str):
        return None
    
    def new_id(self):
        return self.ID_OFFSET if not self.list() else self.list()[-1].id + 1


class SalaRepository(Repository):

    FILE_NAME = "salas.csv"
    ID_OFFSET = 100

    def __init__(self):
        super().__init__(self.FILE_NAME)

    def convert_to_model(self, row: str):
        id, capacidade, ativa, tipo, descricao = row.strip().split(",")
        return Sala(int(id), int(capacidade), ativa, tipo, descricao)


salaRepository = SalaRepository()