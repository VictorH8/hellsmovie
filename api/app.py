import requests

url = "https://beae12aea934a86fee7a488d62819c35.serveo.net/criar"


dados = {'usuario': 'muzan', 'senha': 'dev'}
p = requests.post(url,data=dados)
if p.status_code == 200:
    print("POST FEITO COM SUCESSO")
else:
    print(f"Error: {p.status_code}")

    