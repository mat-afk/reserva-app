class Repository:

    DATABASE_PATH = "/database"

    def _init_(self, source_path=""):
        self.file_path = self.DATABASE_PATH + source_path

    def list(self):
        with open(self.file_path) as file:
            return [self.row_to_model(row) for row in file]

    def save(self, model):
        with open(self.file_path, "a") as file:
            row = self.model_to_row(model)
            file.write(row)

    def model_to_row(self, model):
        pass

    def row_to_model(self, row: str):
        pass


# Exemplo

class Animal:
    def _init_(self, nome, idade):
        super()._init_()
        self.nome = nome
        self.idade = idade


class AnimalRepository(Repository):

    def _init_(self, source_path="animais.csv"):
        super()._init_(source_path)

    def model_to_row(self, model: Animal):
        return f"{model.nome},{model.idade}"

    def row_to_model(self, row: str):
        nome, idade = row.strip().split(",")
        return Animal(nome, idade)


repo = AnimalRepository()
