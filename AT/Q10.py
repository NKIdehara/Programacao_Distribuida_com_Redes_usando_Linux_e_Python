from scapy.all import sniff, IP

def capturar_pacotes(pacote):
    if IP in pacote: # somente pacotes IP
        print(f"Pacote: {pacote[IP].src} -> {pacote[IP].dst}")

# capturar pacotes
sniff(prn=capturar_pacotes, store=0)
