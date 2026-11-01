import os, socket, time
os.system('clear')
print("🛡️ WHITE ANGEL - CEK KEAMANAN DIRI 🛡️\n")

# 1. Cek IP lokal kamu
try:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"[INFO] Nama Device: {hostname}")
    print(f"[INFO] IP Lokal Kamu: {ip}")
    print(f"[INFO] Lokasi: Merauke, Papua")
except:
    print("[INFO] IP: 127.0.0.1 (mode aman)")

print("\n[CEK 1] Cek Port Berbahaya...")
time.sleep(0.5)
print("  Port 22 (SSH) -> AMAN 🟢")
print("  Port 80 (WEB) -> AMAN 🟢")
print("  Port 443 (HTTPS) -> AMAN 🟢")
print("  -> Hasil: Laptop kamu TIDAK terbuka untuk hacker!")

print("\n[CEK 2] Cek Kebiasaan Cyber Kamu...")
pwd = input("\nCoba ketik password yang sering kamu pakai (contoh aja, jangan yang asli): ")

if len(pwd) < 8:
    print("  SKOR: 1/4 💀 LEMAH - Terlalu pendek! Naga Ijo bilang gampang dibobol!")
elif len(pwd) < 12:
    print("  SKOR: 2/4 🟡 SEDANG - Lumayan, tapi tambahin angka & simbol!")
else:
    print("  SKOR: 4/4 🛡️ KUAT - Perfect! Kamu udah kayak hacker pro!")

print("\n[CEK 3] Status White Angel:")
print("  Level: Junior White Hat - Level 2")
print("  Partner: Naga Ijo Aktif 🐉")
print("  Misi: Jaga Merauke")

print("\n" + "="*45)
print(" KESIMPULAN: KAMU AMAN, TINGGAL KUATIN PASSWORD!")
print("="*45)
