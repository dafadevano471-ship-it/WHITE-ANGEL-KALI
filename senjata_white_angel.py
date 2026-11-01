import socket, random, string
from datetime import datetime

def scan():
    target = input("Target scan (localhost aja ya): ")
    if target != "localhost" and target != "127.0.0.1":
        print("❌ Junior Defender cuma boleh scan laptop sendiri!")
        return
    print(f"\n🐉 Naga mulai patroli ke {target}...")
    for port in [22, 80, 443, 3306, 8080]:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            print(f" Port {port}: BUKA")
        else:
            print(f" Port {port}: TUTUP AMAN")
        s.close()

def cek_password():
    pwd = input("Masukin password kamu: ")
    skor = 0
    if len(pwd) >= 8: skor+=1
    if any(c.isupper() for c in pwd): skor+=1
    if any(c.islower() for c in pwd): skor+=1
    if any(c.isdigit() for c in pwd): skor+=1
    if any(c in "!@#$%" for c in pwd): skor+=1
    print(f"Skor: {skor}/5 - {'AMAN 🛡️' if skor>=4 else 'BAHAYA 💀'}")

def bikin_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    pwd = ''.join(random.choice(chars) for _ in range(16))
    print(f"\n🔐 Password Dewa: {pwd}")

while True:
    print("""
╔════════════════════════════════╗
║  SENJATA WHITE ANGEL V1 - 🐉   ║
║  1. Scan Port (Patroli)       ║
║  2. Cek Password Lemah        ║
║  3. Bikin Password Dewa       ║
║  4. Keluar                    ║
╚════════════════════════════════╝
    """)
    pilih = input("Pilih senjata (1-4): ")
    if pilih == "1": scan()
    elif pilih == "2": cek_password()
    elif pilih == "3": bikin_password()
    elif pilih == "4": 
        print("Naga tidur dulu... zzz")
        break
    else: print("Pilih 1-4 aja!")
