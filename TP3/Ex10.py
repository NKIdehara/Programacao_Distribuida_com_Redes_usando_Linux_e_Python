import requests

def cliente_web(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print("Resposta do servidor:")
            print(resposta.text)
        else:
            print(f"Erro ao acessar {url}. Status: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

url = "http://localhost:8000"
cliente_web(url)
