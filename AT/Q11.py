from scapy.all import sniff, ARP

def arp_spoof(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:
        print(f"!!! ARP Spoofing: {pacote[ARP].psrc} -> {pacote[ARP].hwsrc}")

print("Monitorando pacotes ARP.")
sniff(store=0, prn=arp_spoof, filter="arp")
