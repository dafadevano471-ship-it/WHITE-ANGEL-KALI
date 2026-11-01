import time, os, random
os.system('clear')

print("""
 ██████╗██╗   ██╗██████╗ ███████╗██████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
   WHITE ANGEL CYBER SYSTEM v2.0
""")
time.sleep(0.5)

# Animasi loading cyber
for i in range(3):
    print(f"[CYBER] Mengaktifkan jaringan... {'.'*i}", end='\r')
    time.sleep(0.4)
print("\n")

targets = ["127.0.0.1", "localhost", "192.168.1.1"]
for target in targets:
    print(f"\n>>> SCANNING TARGET: {target}")
    for port in [21, 22, 80, 443, 3306]:
        status = random.choice(["CLOSED 🟢 AMAN", "CLOSED 🟢 AMAN", "CLOSED 🟢 AMAN", "FILTERED 🟡"])
        print(f"  [PORT {port}] -> {status}")
        time.sleep(0.08)

print("\n[CYBER CHAT LOG - CEPAT]")
chats = [
    "White Angel > Masuk ke sistem...",
    "Naga Ijo > Firewall aktif!",
    "System > Mendeteksi 0 ancaman",
    "White Angel > Patroli Merauke selesai",
    "Server > ACCESS GRANTED untuk White Angel 🛡️",
]
for c in chats:
    print(c)
    time.sleep(0.12)

print("\n" + "="*40)
print(" CYBER STATUS: AMAN TERKENDALI - MERAUKE SECURE")
print("="*40)
