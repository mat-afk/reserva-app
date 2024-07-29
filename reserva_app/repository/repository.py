from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala, SalaType
from reserva_app.domain.model import Model
from pathlib import Path

class Repository:

    DATABASE_PATH = Path(__file__).resolve().parents[2] / "database"
    ID_OFFSET = 1

    def __init__(self, source_path: str):
        self.file_path = self.DATABASE_PATH / source_path

        if not self.file_path.parent.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, model: Model) -> int:
        model.id = self.new_id()
        row = model.to_row()
        
        with open(self.file_path, "a") as file:
            file.write(row)

        return model.id

    def find_all(self) -> list[Model]:
        if not self.file_path.exists():
            return []
        
        with open(self.file_path) as file:
            return [self.convert_to_model(row) for row in file]

    def find_by_id(self, id: int) -> Model:
        for model in self.find_all():
            if model.id == id:
                return model
            
        return None
    
    def update(self, id: int, model: Model):
        if not self.file_path.exists(): return

        rows = []

        with open(self.file_path, "r") as file:
            for row in file:
                fields = row.strip().split(",")

                if id == int(fields[0]):
                    rows.append(model.to_row())
                else:
                    rows.append(row)

        with open(self.file_path, "w") as file:
            file.writelines(rows)

    def delete(self, id: int):
        if not self.file_path.exists(): return
        
        remaining_rows = []

        with open(self.file_path, "r") as file:
            for row in file:
                fields = row.strip().split(",")

                if id != int(fields[0]):
                    remaining_rows.append(row)

        with open(self.file_path, "w") as file:
            file.writelines(remaining_rows)
                    
    def convert_to_model(self, row: str) -> Model:
        return None
    
    def split_fields(self, row: str) -> list[str]:
        fields = []
        current = []
        in_quotes = False

        i = 0
        while i < len(row):
            char = row[i]

            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                fields.append(''.join(current).strip())
                current = []
            else:
                current.append(char)

            i += 1

        fields.append(''.join(current).strip())

        for i in range(len(fields)):
            if fields[i].startswith('"') and fields[i].endswith('"'):
                fields[i] = fields[i][1:-1].replace('""', '"')

        return fields
    
    def str_to_bool(self, text: str) -> bool:
        return text.strip().lower() in ("true", "1")
    
    def new_id(self) -> int:
        models = self.find_all()
        return self.ID_OFFSET if not models else models[-1].id + 1
    

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


usuarioRepositoy = UsuarioRepository()

salaRepository = SalaRepository()