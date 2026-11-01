import socket

target = "testphp.vulnweb.com"
ports = [21, 22, 53, 80, 443, 3306]

print(f"[NAGA] Mengintip {target}...")
for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[TERBUKA] Port {port} -> Mungkin ada harta!")
    else:
        print(f"[TUTUP] Port {port} aman")
    s.close()
0

