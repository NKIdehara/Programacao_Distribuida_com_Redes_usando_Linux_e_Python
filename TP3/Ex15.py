import http.server
import socketserver
import ssl

PORT = 8000
CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

class ServidorHTML(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'helloworld.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

httpd = socketserver.TCPServer(("", PORT), ServidorHTML)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
print(f"Servidor na porta {PORT}")
httpd.serve_forever()
