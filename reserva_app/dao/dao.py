from typing import TypeVar
from reserva_app.domain.usuario import Usuario
from reserva_app.domain.sala import Sala
from reserva_app.domain.reserva import Reserva
from reserva_app.db.connection import create_connection, close_connection

T = TypeVar("T", Usuario, Sala, Reserva)

class DAO:

    def save(self, model: T) -> None: pass
    def update(self, model: T) -> T: pass
    def find_by_id(self, id: int) -> T: pass
    def find_all(self) -> list[T]: pass
    def delete(self, id: int) -> None: pass
    def generate_model(self, result) -> T: pass
    
    def execute(self, sql: str, params: tuple) -> None:
        with create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)

            conn.commit()

    def query(self, sql: str, params: tuple = None) -> list[T]:
        with create_connection() as conn:
            with conn.cursor(dictionary = True) as cursor:
                cursor.execute(sql, params)
                return [model for model in [self.generate_model(result) for result in cursor.fetchall()]]