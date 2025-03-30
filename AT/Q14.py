import requests

URL = "http://infnet.edu.br"
lista = ["admin", "login", "dashboard", "config", "infnet"]

print(f"Web fuzzing em {URL}:")
for path in lista:
    url = f"{URL}/{path}"
    response = requests.get(url, timeout=5)
    print(f"(verificando exposição) {url} -> {response.status_code}")
