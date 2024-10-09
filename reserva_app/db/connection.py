import mysql.connector

def open_connection(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def close_connection(conn):
    conn.close

conn = open_connection("localhost", "estudante1", "estudante1", "")