from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask (__name__)

@app.route("/")
def home():
    dicionario = repositorio.retornar_personagens()
    return render_template("index.html", dados = dicionario)

@app.route("/personagem/<int:id>", methods = ['GET', 'POST'])
def editar_personagem(id):

    if request.method == 'POST':
        #quer dizer que o usuario esta mandando dados
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect (url_for('home'))
        elif "salvar" in request.form:
            personagem = {}
            personagem['usuario'] = request.form["usuario"]
            personagem['personagem'] = request.form["personagem"]
            personagem['origem'] = request.form["origem"]
            personagem['level'] = request.form["level"]
            personagem['vida'] = request.form["vida"]
            personagem['dinheiro'] = request.form["dinheiro"]

            if id in repositorio.personagens.keys():
                repositorio.atualizar_personagem(id, personagem)
            
            return redirect(url_for('home'))
    else:
    
        #retorna os dados de um personagem na pagina de cadastro
        personagem = repositorio.retornar_personagem(id)
        personagem['id'] = id
        return render_template("cadastro.html", **personagem)

@app.route("/personagem", methods = ["GET", "POST"])
def criar_personagem():
    if request.method == "POST":
            personagem = {}
            personagem['usuario'] = request.form["usuario"]
            personagem['personagem'] = request.form["personagem"]
            personagem['origem'] = request.form["origem"]
            personagem['level'] = request.form["level"]
            personagem['vida'] = request.form["vida"]
            personagem['dinheiro'] = request.form["dinheiro"]
            repositorio.criar_personagem(**personagem)
            return redirect(url_for('home'))
    else:
        return render_template('cadastro.html', id=repositorio.gerar_id())

app.run(debug = True)