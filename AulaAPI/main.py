from flask import Flask, jsonify, request, redirect, url_for
import repositorio

app = Flask (__name__)

#ROTA PARA RETORNAR TODOS OS PERSONAGENS
@app.route("/personagens", methods = ['GET'])
def get_personagens():
    lista_personagens = repositorio.retornar_personagens()
    return jsonify(lista_personagens)
    

#ROTA PARA RETORNAR UM UNICO PERSONAGEM
@app.route("/personagem/<int:id>", methods = ['GET'])
def get_personagem(id):
    personagem = repositorio.retornar_personagem(id)

    if personagem:
        return jsonify(personagem)
    else:
        return jsonify({"message": "Personagem não encontrado"}), 404 

@app.route("/personagem", methods = ["POST"])
def criar_personagem():
    personagem = request.json
    id_personagem = repositorio.criar_personagem(**personagem)
    personagem["id"] = id_personagem
    return jsonify(personagem), 201


#ROTA PARA ALTERAR UM PERSONAEGEM
@app.route("/personagem/<int:id>", methods = ['PUT'])
def atualizar_personagem(id):
    personagem = repositorio.retornar_personagem(id)
    if personagem:
        dados_atualizados = request.json
        dados_atualizados["id"] = id
        repositorio.atualizar_personagem(**dados_atualizados)
        return(jsonify(dados_atualizados))
    else:
        return jsonify({"message": "Personagem não encontrado"}), 404


#ROTA PARA DELETAR UM PERSONAGEM
@app.route("/personagem/<int:id>", methods = ["DELETE"])
def remover_personagem(id):
    personagem = repositorio.retornar_personagem(id)
    if personagem:
        repositorio.remover_personagem(id)
        return jsonify({"message":"Personagem removido com sucesso"})
    else:
        return jsonify({"message":"Personagem não encontrado"}), 404


app.run(debug = True)