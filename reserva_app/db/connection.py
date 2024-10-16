import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def open_connection(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def close_connection(conn):
    conn.close()

def create_connection():
    return open_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

class Connection:
    HOST: str = DB_HOST
    USER: str =  DB_USER
    PASSWORD: str = DB_PASSWORD
    DATABASE: str = DB_NAME

    def __init__(self):
        self.__conn = self.open(self.HOST, self.USER, self.PASSWORD, self.DATABASE)

    def open(self, host, user, password, database):
        return mysql.connector.connect(host=host, user=user, password=password, database=database)

    def close(self):
        self.__conn.close()