from reserva_app.db.connection import open_connection, close_connection
from reserva_app.db.user_manager import *
from reserva_app.db.tables import create_tables

conn = open_connection("localhost", "estudante1", "estudante1", "reserva")

create_tables(conn)

conn.reconnect()

insert_user(conn, 1, "Marino", "email@email.com", "1234", True, False)

list_user(conn)

close_connection(conn)