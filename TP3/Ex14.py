import ssl
import socket

def obter_certificado(endereco, porta=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((endereco, porta)) as sock:
            with context.wrap_socket(sock, server_hostname=endereco) as ssock:
                certificado = ssock.getpeercert()
                return certificado
    except Exception as e:
        print(f"Erro ao obter o certificado SSL: {e}")
        return None

def ler_certificado(certificado):
    if not certificado:
        print("Nenhum certificado recuperado.")
        return
    print("Informações do Certificado:")
    print(certificado)

endereco = "www.infnet.edu.br"
print(f"Página web: {endereco}")
certificado = obter_certificado(endereco)
ler_certificado(certificado)
