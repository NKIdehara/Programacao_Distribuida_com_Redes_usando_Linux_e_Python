import http.server
import socketserver

PORT = 8000

class ServidorHTML(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'helloworld.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), ServidorHTML) as httpd:
    print(f"Servidor na porta {PORT}")
    httpd.serve_forever()