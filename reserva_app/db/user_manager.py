from db.connection import close_con, open_con

def list_user(con):
    cursor = con.cursor(dictionary = True)
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    for registro in cursor:
        print(registro['user_id']+ "-" + registro['nome'])
    cursor.close()
    
def insert_user(con, id, nome, email, senha, ativo, adm):
    cursor = con.cursor()
    sql = "INSERT INTO clientes (user_id, nome, email, senha, ativo, adm) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql, (id, nome, email, senha, ativo, adm))
    con.commit()
    cursor.close()

def remove_user(con, id):
    cursor = con.cursor()
    sql = "REMOVE FROM clientes WHERE user_id = %s"
    cursor.execute(sql, (id))
    con.commit()
    cursor.close()

def is_ativo_user(con, id, ativo):
    cursor = con.cursor()
    sql = "UPDATE cliente SET ativo = %s WHERE user_id = %s"
    cursor.execute(sql, (ativo, id))
    con.commit()
    cursor.close()