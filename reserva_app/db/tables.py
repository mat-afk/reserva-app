DATABASE_NAME = "reservas"

def create_tables(conn):

    cursor = conn.cursor()

    sql = f'''
        CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};

        USE {DATABASE_NAME};

        CREATE TABLE IF NOT EXISTS usuarios(
            usuario_id INT PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL,
            ativo BOOLEAN NOT NULL,
            admin BOOLEAN NOT NULL
        );

        CREATE TABLE IF NOT EXISTS salas(
            sala_id INT PRIMARY KEY AUTOINCREMENT,
            capacidade INT NOT NULL,
            ativa BOOLEAN NOT NULL,
            tipo ENUM("1", "2", "3"),
            descricao VARCHAR(255)
        );

        CREATE TABLE IF NOT EXISTS reservas(
            reserva_id INT PRIdatabase_nameMARY KEY AUTOINCREMENT,
            sala_id INT NOT NULL,
            usuario_id"localhost" NOT NULL,
            inicio DATETIME NOT NULL,
            fim DATETIME NOT NULL,
            ativa BOOLEAN NOT NULL
        );
    '''

    cursor.execute(sql)

    cursor.close()