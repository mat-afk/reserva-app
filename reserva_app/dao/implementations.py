from datetime import datetime
from reserva_app.dao.dao import DAO
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala, SalaType
from reserva_app.domain.reserva import Reserva
from reserva_app.db.connection import *

class UsuarioDAO(DAO):

    TABLE_NAME = "usuarios"

    def save(self, model: Usuario) -> None:
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (usuario_id, nome, email, senha, ativo, admin) 
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        self.execute(sql, (model.id, model.nome, model.email, model.senha, model.ativo, model.admin))

    def update(self, model: Usuario) -> Usuario:

        sql = f"""
            UPDATE {self.TABLE_NAME} 
            SET nome = %s, email = %s, senha = %s, ativo = %s, admin = %s
            WHERE usuario_id = %s;
        """
        self.execute(sql, (model.nome, model.email, model.senha, model.ativo, model.admin, model.id))

    def find_by_id(self, id: int) -> Usuario: 
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE usuario_id = %s;"
        
        models = self.query(sql, params=(id,))
        if models:
            models.pop()

    def find_all(self) -> list[Usuario]:
        sql = f"SELECT * FROM {self.TABLE_NAME};"
        return self.query(sql)

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {self.TABLE_NAME} WHERE usuario_id = %s;"
        self.execute(sql, (id,))

    def generate_model(self, result) -> Usuario:
        return Usuario(
            id=result["usuario_id"],
            nome=result["nome"],
            email=result["email"],
            senha=result["senha"],
            ativo=result["ativo"],
            admin=result["admin"],
        )


class SalaDAO(DAO):

    TABLE_NAME = "salas"

    def save(self, model: Sala) -> None:

        sql = f"""
            INSERT INTO {self.TABLE_NAME} (sala_id, capacidade, ativa, tipo, descricao)
            VALUES (%s, %s, %s, %s, %s);
        """
        self.execute(sql, (model.id, model.capacidade, model.ativa, model.tipo, model.descricao))

    def update(self, model: Sala) -> Sala:

        sql = f"""
            UPDATE {self.TABLE_NAME} 
            SET capacidade = %s, ativa = %s, tipo = %s, descricao = %s
            WHERE sala_id = %s;
        """
        self.execute(sql, (model.capacidade, model.ativa, model.tipo, model.descricao, model.id))

    def find_by_id(self, id: int) -> Sala: 
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE sala_id = %s;"

        models = self.query(sql, params=(id,))
        if models:
            models.pop()

    def find_all(self) -> list[Sala]:
        sql = f"SELECT * FROM {self.TABLE_NAME};"
        return self.query(sql)

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {self.TABLE_NAME} WHERE sala_id = %s;"
        self.execute(sql, (id,))

    def generate_model(self, result) -> Sala:
        return Sala(
            id=result["sala_id"],
            capacidade=result["capacidade"],
            ativa=result["ativa"],
            tipo=SalaType(int(result["tipo"])),
            descricao=result["descricao"],
        )
    

class ReservaDAO(DAO):

    TABLE_NAME = "reservas"

    def save(self, model: Reserva) -> None:

        sql = f"""
            INSERT INTO {self.TABLE_NAME} (reserva_id, sala_id, usuario_id, inicio, fim, ativa)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        self.execute(sql, (model.id, model.sala.id, model.usuario.id, model.inicio, model.fim))

    def update(self, model: Reserva) -> Reserva:

        sql = f"""
            UPDATE {self.TABLE_NAME} 
            SET sala_id = %s, usuario_id = %s, inicio = %s, fim = %s, ativa = %s
            WHERE reserva_id = %s;
        """
        self.execute(sql, (model.sala.id, model.usuario.id, model.inicio, model.fim, model.id))

    def find_by_id(self, id: int) -> Reserva: 
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE reserva_id = %s;"

        models = self.query(sql, params=(id,))
        if models:
            models.pop()

    def find_all(self) -> list[Reserva]:
        sql = f"SELECT * FROM {self.TABLE_NAME};"
        return self.query(sql)

    def delete(self, id: int) -> None:
        sql = f"DELETE FROM {self.TABLE_NAME} WHERE reserva_id = %s;"
        self.execute(sql, (id,))

    def generate_model(self, result) -> Reserva:
        return Reserva(
            id=result["reserva_id"],
            sala=salaDAO.find_by_id(int(result["sala_id"])),
            usuario=usuarioDAO.find_by_id(int(result["usuario_id"])),
            inicio=datetime(result["inicio"]),
            fim=datetime(result["fim"]),
            ativa=result["ativa"],
        )
    

usuarioDAO = UsuarioDAO()
salaDAO = SalaDAO()
reservaDAO = ReservaDAO()

print(reservaDAO.find_all())