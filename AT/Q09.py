from scapy.all import IP, TCP, sr1

host = "localhost"
pacote_ip = IP(dst=host)
for porta in range(0, 9999):
    pacote_tcp = TCP(dport=porta, flags="S")
    resposta = sr1(pacote_ip/pacote_tcp, timeout=5, verbose=0)
    if resposta is not None:
        if resposta.haslayer(TCP):
            if resposta[TCP].flags == 0x12:  # SYN-ACK
                sr1(pacote_ip/TCP(dport=porta, flags="R"), timeout=1, verbose=0)
                print(f"Porta {porta}: ABERTA")
