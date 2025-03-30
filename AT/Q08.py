from scapy.all import sniff, IP, ICMP, TCP, UDP, sendp

INTERFACE = "enp0s3"
FILTER = "icmp"
NUM_PACOTES = 3

def analisar_pacote(pacote):
    print("\nAnalisando pacote")
    if pacote.haslayer(IP):
        print(f"\tOrigem: {pacote[IP].src} -> Destino: {pacote[IP].dst}")
        print(f"\tProtocolo: {pacote[IP].proto}")
    if pacote.haslayer(TCP):
        print(f"\tTCP -> Porta Origem: {pacote[TCP].sport}, Porta Destino: {pacote[TCP].dport}")
    if pacote.haslayer(UDP):
        print(f"\tUDP -> Porta Origem: {pacote[UDP].sport}, Porta Destino: {pacote[UDP].dport}")
    if pacote.haslayer(ICMP):
        print("\tICMP -> Tipo:", pacote[ICMP].type)

def modificar_pacote(pacote):
    if pacote.haslayer(ICMP):
        print("Modificando pacote")
        pacote[IP].src = "192.168.1.100"
        pacote[ICMP].load = b"Modificado!"
        del pacote[IP].chksum
        del pacote[ICMP].chksum
        return pacote
    return None

def injetar_pacote(pacote):
    if pacote:
        print("Injetando pacote")
        sendp(pacote, iface=INTERFACE, verbose=False)

print(f"Capturando pacotes: {INTERFACE}")
pacotes = sniff(iface=INTERFACE, filter=FILTER, count=NUM_PACOTES)
for pacote in pacotes:
    analisar_pacote(pacote)
    pacote = modificar_pacote(pacote)
    injetar_pacote(pacote)