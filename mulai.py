import socket, time, os, random, string

# BANNER WHITE ANGEL
def banner():
    os.system('clear')
    print("""
██╗    ██╗██╗  ██╗██╗████████╗███████╗     █████╗ ███╗   ██╗ ██████╗ ███████╗██╗     
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝    ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     
██║ █╗ ██║███████║██║   ██║   █████╗      ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     
██║███╗██║██╔══██║██║   ██║   ██╔══╝      ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     
╚███╔███╔╝██║  ██║██║   ██║   ███████╗    ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝
    JUNIOR WHITE HAT HACKER - Partner: Naga Ijo 🐉
    Motto: PROTECT > DEFEND > LEARN
""")

def loading():
    print("[*] Membangunkan Naga Ijo...")
    time.sleep(1)
    print("[*] Mengecek Firewall...")
    time.sleep(1)
    print("[*] ACCESS GRANTED... 🟢\n")

def scan_diri():
    print("=== PATROLI LAPTOP SENDIRI ===")
    for port in [22, 80, 443]:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex(("127.0.0.1", port))
        status = "BUKA" if result == 0 else "AMAN"
        print(f" Port {port} : {status}")
        s.close()

def cek_pwd():
    pwd = input("\nMasukin password buat di cek: ")
    skor = 0
    if len(pwd) >= 8: skor+=1
    if any(c.isupper() for c in pwd): skor+=1
    if any(c.isdigit() for c in pwd): skor+=1
    if any(c in "!@#$%" for c in pwd): skor+=1
    print(f" Skor keamanan: {skor}/4 {'🛡️ KUAT' if skor>=3 else '💀 LEMAH'}")

# MULAI
banner()
loading()
print(f"Selamat datang, White Angel!")
print(f"Waktu: {time.ctime()}\n")
scan_diri()
cek_pwd()
print("\n[+] Misi hari ini selesai. Naga kembali tidur.")
