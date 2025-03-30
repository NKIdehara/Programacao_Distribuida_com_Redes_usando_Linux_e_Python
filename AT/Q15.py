import nmap

alvo = "192.168.1.181"
portas = "22,23,80,443,8080,8443,8000,8888,9000,1080,2082,2083,2095,2096,3128,5985,5986,8008,8010,8081,8181,8282,8444,8880,9443"

scanner = nmap.PortScanner()
print(f"Varredura em {alvo} nas portas {portas}:")
scanner.scan(alvo, portas, arguments="-T4 -sS")
for host in scanner.all_hosts():
    print(f"Host: {host} ({scanner[host].hostname()})")
    print(f"Status: {scanner[host].state()}")
    for port in scanner[host]["tcp"]:
        if scanner[host]["tcp"][port]["state"] == "open":
            print(f"Porta {port}: ABERTA")
        elif scanner[host]["tcp"][port]["state"] == "closed":
            print(f"Porta {port}: fechada")
