print("🐉 Naga Linux mulai patroli...")
print("Mengecek localhost (laptop kamu sendiri)...")

import socket
port_bahaya = [21, 22, 23, 80, 445, 3389]
for port in port_bahaya:
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect(("127.0.0.1", port))
        print(f"[!] Port {port} TERBUKA - hati-hati!")
    except:
        print(f"[AMAN] Port {port} tertutup")
    s.close()

print("\nPatroli selesai. Laporan siap!")
