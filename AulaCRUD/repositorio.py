#ESTE SCRIPT SIMULA FUNCIONALIDADES DE BD PARA O PROJETO DE CRUD

#O dicionario eh nosso repositorio principal
personagens = {
    1:{
        "usuario": "Alisson",
        "personagem": "Sven",
        "origem": "Imperial",
        "level": "7",
        "vida": "10",
        "dinheiro":"100"
    },
    2:{
        "usuario": "Pedro",
        "personagem": "Bob",
        "origem": "Nordicos",
        "level": "7",
        "vida": "10",
        "dinheiro": "1000"
    },
    3:{
        "usuario": "Felype",
        "personagem": "Orin",
        "origem": "Extremo Norte",
        "level":"7",
        "vida": "8",
        "dinheiro": "10"
    },
}

#funcao que gera um novo id
def gerar_id():
    id = len(personagens) +1
    return id

#funcao que gera novo personagem no dicionario
def criar_personagem(usuario, personagem, origem, level, vida, dinheiro):
    personagens[gerar_id()] = {
        "usuario": usuario,
        "personagem": personagem,
        "origem": origem,
        "level": level,
        "vida": vida,
        "dinheiro": dinheiro
    }

#funcao retorna um dicionario com todos os personagens
def retornar_personagens():
    return personagens

#funcao retorna um unico personagem do dicionario
def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}

#funcao atualiza os dados de um personagem do dicionario
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem 

#funcao remove um personagem do dicionario
def remover_personagem(id:int):
    del personagens[id]



#criar_personagem("Daniel", "Dan", "Nordicos", "8", "10", "1000")

#print(retornar_personagem(4))
#remover_personagens(4)


#funcao para retorno esta apresentando erro
#print(retornar_personagens)