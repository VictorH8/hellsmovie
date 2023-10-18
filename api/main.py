# IMPORTAÇÃO DE MODULOS/LIBS
from flask import Flask, render_template, request
import requests
import json

# INICIA A APLICAÇÃO FLASK
app = Flask(__name__)

# GERA A ROTA PRINCIPAL DO PROJETO
@app.route('/', methods=['GET', 'POST'])
def home():
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=pt-BR&page=90&sort_by=popularity.desc"
    headers = {"accept": "application/json","Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMmM2YWNkNDM4OTVjZGVlMzkwNWRhODhjZDdjOTNjZiIsInN1YiI6IjY1MGYxYWQ2MjZkYWMxMDEyZDVhOTRjYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P2xiPnZCI13rJqk-Pe7KWfIgVRbYf80777VvzGoNdik"}

    # FAZ A REQUISIÇÃO
    response = requests.get(url, headers=headers)

    #VERIFICA SE A REQUISIÇÃO TEM O STATUS CODE 200
    if response.status_code == 200:
        dados = response.json()
        resultados = dados['results']

        filmes = []

        for filme in resultados:
            titulo = filme['title']
            resumo = filme['overview']
            data_lancamento = filme['release_date']
            popularidade = filme['popularity']
            icon = filme.get('backdrop_path')
            idmovie = filme['id']

            if icon:
                foto = f"https://image.tmdb.org/t/p/w500/{icon}"
            else:
                foto = "/static/images/default.jpg"

            filme_info = {
                'titulo': titulo,
                'resumo': resumo,
                'data_lancamento': data_lancamento,
                'popularidade': popularidade,
                'foto': foto,
                'id': idmovie
            }

            filmes.append(filme_info)

        return render_template('index.html', res=filmes)
    else:
        return f"Erro status code: {response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)
