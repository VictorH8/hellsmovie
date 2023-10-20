from flask import Flask, render_template, request, jsonify
import requests
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=pt-BR&page=90&sort_by=popularity.desc"
    headers = {"accept": "application/json","Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMmM2YWNkNDM4OTVjZGVlMzkwNWRhODhjZDdjOTNjZiIsInN1YiI6IjY1MGYxYWQ2MjZkYWMxMDEyZDVhOTRjYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P2xiPnZCI13rJqk-Pe7KWfIgVRbYf80777VvzGoNdik"}

    response = requests.get(url, headers=headers)

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
                'id': idmovie,
                'movie': f'https://themoviedbbot.blogspot.com/?mv1={idmovie}'
            }

            filmes.append(filme_info)

        return render_template('index.html', res=filmes)
    else:
        return f"Erro status code: {response.status_code}"
    

TMDB_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMmM2YWNkNDM4OTVjZGVlMzkwNWRhODhjZDdjOTNjZiIsInN1YiI6IjY1MGYxYWQ2MjZkYWMxMDEyZDVhOTRjYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P2xiPnZCI13rJqk-Pe7KWfIgVRbYf80777VvzGoNdik'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        pesquisa_filme = request.form.get('query')
        url = f"https://api.themoviedb.org/3/search/movie?query={pesquisa_filme}&include_adult=true&language=pt-BR&page=1"
        
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_KEY}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            return render_template('search.html', dados=dados)
        else:
            return f"Erro na pesquisa. Status code: {response.status_code}"

    return render_template('search.html', dados=None)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run(debug=True)
