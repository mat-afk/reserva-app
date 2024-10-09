def list_user(con):
    cursor = con.cursor(dictionary = True)
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    for registro in cursor:
        print(registro['usuario_id']+ "-" + registro['nome'])
    cursor.close()
    
def insert_user(conn, id, nome, email, senha, ativo, adm):
    cursor = conn.cursor()
    sql = "INSERT INTO usuarios(usuario_id, nome, email, senha, ativo, adm) VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (id, nome, email, senha, ativo, adm))
    conn.commit()
    cursor.close()

def remove_user(con, id):
    cursor = con.cursor()
    sql = "REMOVE FROM usuarios WHERE usuario_id = %s"
    cursor.execute(sql, (id))
    con.commit()
    cursor.close()

def is_ativo_user(con, id, ativo):
    cursor = con.cursor()
    sql = "UPDATE usuarios SET ativo = %s WHERE usuario_id = %s"
    cursor.execute(sql, (ativo, id))
    con.commit()
    cursor.close()