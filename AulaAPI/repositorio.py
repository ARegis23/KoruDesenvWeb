import sqlite3

#funcao que gera um novo id
def gerar_id():
    conn = sqlite3.connect("RPG.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = 'personagens'")
    next_id = cursor.fetchone()[0]
    return next_id + 1

#funcao que CRIA novo personagem no dicionario
def criar_personagem(usuario, personagem, origem, level, vida, dinheiro):
    try:
        conn = sqlite3.connect("RPG.db")
        cursor = conn.cursor()
        sql_insert = " INSERT INTO personagens (usuario_personagem, personagem_personagem, origem_personagem, level_personagem, vida_personagem, dinheiro_personagem) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (usuario, personagem, origem, level, vida, dinheiro))
        personagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return personagem_id
    except Exception as ex:
        print(ex)
        return 0

#funcao RETORNA um dicionario com todos os personagens
def retornar_personagens():
    try:
        resultado = []
        conn = sqlite3.connect("RPG.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens"
        cursor.execute(sql_select)
        personagens = cursor.fetchall()
        conn.close()
        for item in personagens:
            personagem = {
                'id': item[0],
                'usuario': item[1],
                'personagem': item[2],
                'origem': item[3],
                'level': item[4],
                'vida': item[5],
                'dinheiro': item[6]
            }
            resultado.append(personagens)
        return resultado
    except:
        return False

#funcao RETORNA um unico personagem do dicionario
def retornar_personagem(id:int):
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", "",""
        conn = sqlite3.connect("RPG.db")
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_select, (id, ))
        id, usuario, personagem, origem, level, vida, dinheiro = cursor.fetchone()
        conn.close()
        return {"id": id,
                "usuario": usuario,
                "personagem": personagem,
                "origem": origem, 
                "level": level, 
                "vida": vida, 
                "dinheiro": dinheiro
            }
    except:
        return False

#funcao ATUALIZA os dados de um personagem do dicionario
def atualizar_personagem(id:int, usuario, personagem, origem, level, vida, dinheiro):
    try:
        #tentar atualizar
        conn = sqlite3.connect("RPG.db")
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET usuario_personagem = ?, personagem_personagem = ?, origem_personagem = ?, level_personagem = ?, vida_personagem = ?, dinheiro_personagem = ? WHERE id_personagem = ?"
        cursor.execute(sql_update, (usuario, personagem, origem, level, vida, dinheiro, id))
        conn.commit()
        conn.close()
        return True

    except Exception as ex:
        print(ex)
        return False

#funcao REMOVE um personagem do dicionario
def remover_personagem(id:int):
    try:
        conn = sqlite3.connect("RPG.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

'''
#testes:

usuario = "Alisson"
personagem = "Sven"
origem = "Imperial"
level = "7"
vida = "10"
dinheiro = "100"

id = criar_personagem(usuario, personagem, origem, level, vida, dinheiro)
print(id)
print(retornar_personagem(id))

id, usuario, personagem, origem, level, vida, dinheiro = retornar_personagem(id)
atualizar_personagem(id, "Alisson Regis", personagem, origem, level, vida, dinheiro)

print(retornar_personagem(id))
id, usuario, personagem, origem, level, vida, dinheiro = retornar_personagem(id)

print(retornar_personagens())

#remover_personagem(id)

print(retornar_personagens())
'''