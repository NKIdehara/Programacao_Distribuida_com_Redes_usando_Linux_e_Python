import socket

def escanear_portas(endereco, portas):
    print(f"endereço: {endereco}")
    for porta in portas:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.settimeout(1)
        resposta = conexao.connect_ex((endereco, porta))
        if resposta == 0:
            print(f"porta {porta} aberta")
        else:
            print(f"porta {porta} fechada")
        conexao.close()

endereco = "www.microsoft.com"
portas = (21, 22, 23, 25, 53, 110, 3306, 80, 443)
escanear_portas(endereco, portas)
