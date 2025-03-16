import http.server
import socketserver

PORT = 8000
DIRECTORY = "."

class ServidorArquivos(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), ServidorArquivos) as httpd:
    print(f"Servidor de arquivos na porta {PORT}.")
    httpd.serve_forever()