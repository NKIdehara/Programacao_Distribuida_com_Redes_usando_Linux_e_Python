import ssl

protocolos = [
    (ssl.PROTOCOL_SSLv23, "PROTOCOL_SSLv23"),
    (ssl.PROTOCOL_TLS, "PROTOCOL_TLS"),
    (ssl.PROTOCOL_TLS_CLIENT, "PROTOCOL_TLS_CLIENT"),
    (ssl.PROTOCOL_TLS_SERVER, "PROTOCOL_TLS_SERVER"),
    (ssl.PROTOCOL_TLSv1, "PROTOCOL_TLSv1"),
    (ssl.PROTOCOL_TLSv1_1, "PROTOCOL_TLSv1_1"),
    (ssl.PROTOCOL_TLSv1_2, "PROTOCOL_TLSv1_2")
]

def conectar(protocolo):
    try:
        ctx = ssl.SSLContext(protocolo[0])
        print(f"{protocolo[1]}: Suportado")
    except:
        print(f"{protocolo[1]}: Não suportado")

for protocolo in protocolos:
    conectar(protocolo)