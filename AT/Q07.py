import pcapy

INTERFACE = "enp0s3"
FILTER = "icmp"
MAX_PACKET_SIZE = 65536

def capturar_pacote(header, pacote):
    print(f"Pacote: {header.getlen()} bytes")
    injetar_pacote(pacote)

def injetar_pacote(pacote):
    emissor = pcapy.open_live(INTERFACE, MAX_PACKET_SIZE, 1, 0)
    emissor.sendpacket(pacote)
    print("Pacote injetado.")

print(f"Iniciando captura: {INTERFACE}")
pacote = pcapy.open_live(INTERFACE, MAX_PACKET_SIZE, 1, 0)
pacote.setfilter(FILTER)
pacote.loop(-1, capturar_pacote)
