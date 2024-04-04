from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask (__name__)

@app.route("/")
def home():
    lista_personagens = repositorio.retornar_personagens()
    return render_template("index.html", dados = lista_personagens)

@app.route("/personagem/<int:id>", methods = ['GET', 'POST'])
def editar_personagem(id):

    if request.method == 'POST':
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect (url_for('home'))
        elif "salvar" in request.form:
            id = request.form["id"]
            usuario = request.form["usuario"]
            personagem = request.form["personagem"]
            origem = request.form["origem"]
            level = request.form["level"]
            vida = request.form["vida"]
            dinheiro = request.form["dinheiro"]

            dados_retornados = repositorio.retornar_personagem(id)
            if dados_retornados:
                repositorio.atualizar_personagem(id = id, usuario = usuario, personagem = personagem, origem = origem, level = level, vida = vida, dinheiro = dinheiro)
            else:
                repositorio.criar_personagem(usuario= usuario, personagem= personagem, origem= origem, level= level, vida= vida, dinheiro= dinheiro)
            
            return redirect(url_for('home'))
    else:
        #retorna os dados de um personagem na pagina de cadastro
        id, usuario, personagem, origem, level, vida, dinheiro = repositorio.retornar_personagem(id)
        
        return render_template("cadastro.html", id = id, usuario = usuario, personagem = personagem, origem = origem, level = level, vida = vida, dinheiro = dinheiro)

app.run(debug = True)