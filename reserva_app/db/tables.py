from reserva_app.db.connection import *

DATABASE_NAME = "reserva_app"

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    sql = f'''
        CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};

        USE {DATABASE_NAME};

        CREATE TABLE IF NOT EXISTS usuarios(
            usuario_id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha VARCHAR(255) NOT NULL,
            ativo BOOLEAN NOT NULL,
            admin BOOLEAN NOT NULL
        );

        CREATE TABLE IF NOT EXISTS salas(
            sala_id INT PRIMARY KEY AUTO_INCREMENT,
            capacidade INT NOT NULL,
            ativa BOOLEAN NOT NULL,
            tipo ENUM("1", "2", "3"),
            descricao VARCHAR(255)
        );

        CREATE TABLE IF NOT EXISTS reservas(
            reserva_id INT PRIMARY KEY AUTO_INCREMENT,
            sala_id INT NOT NULL,
            usuario_id INT NOT NULL,
            inicio DATETIME NOT NULL,
            fim DATETIME NOT NULL,
            ativa BOOLEAN NOT NULL,

            FOREIGN KEY (sala_id) REFERENCES salas(sala_id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
        );
    '''

    for statement in sql.split(";"):
        cursor.execute(statement.strip())

    cursor.close()

    close_connection(conn)