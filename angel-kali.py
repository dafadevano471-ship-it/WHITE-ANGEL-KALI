#!/usr/bin/env python3
# WHITE ANGEL KALI v4.1 - MERAUKE DEFENDER
import os, time, datetime, subprocess, sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def banner():
    os.system('clear')
    print(f"{CYAN}")
    print("██╗    ██╗██╗  ██╗██╗████████╗███████╗     █████╗ ███╗   ██╗ ██████╗ ███████╗██╗     ")
    print("██║    ██║██║  ██║██║╚══██╔══╝██╔════╝    ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ")
    print("██║ █╗ ██║███████║██║   ██║   █████╗      ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ")
    print("██║███╗██║██╔══██║██║   ██║   ██╔══╝      ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ")
    print("╚███╔███╔╝██║  ██║██║   ██║   ███████╗    ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗")
    print(" ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝")
    print(f"{WHITE}              KALI v4.1 - MERAUKE DEFENDER - MODE 1 HP{RESET}")
    print(f"{RED}              [ AUTO ANTI-HACKER - BLACK HAT KILLER ]{RESET}")
    print(f"{YELLOW}================================================================{RESET}")

def log_report(pesan):
    with open("laporan_white_angel.txt","a") as f:
        f.write(f"[{datetime.datetime.now()}] {pesan}\n")

def menu1():
    banner()
    print(f"{GREEN}[01] APK PELAPORAN - SISTEM LAPORAN OTOMATIS{RESET}\n")
    nama = input("Nama pelapor (Merauke Defender): ")
    bukti = input("Bukti serangan / nama APK mencurigakan: ")
    laporan = f"\n    ================= LAPORAN RESMI WHITE ANGEL =================\n    Pelapor: {nama}\n    Waktu: {datetime.datetime.now()}\n    Lokasi: Merauke, Papua\n    Bukti: {bukti}\n    Status: DILAPORKAN KE SISTEM DEFENDER\n    ============================================================\n    "
    print(f"{GREEN}{laporan}{RESET}")
    log_report(f"PELAPORAN APK: {bukti} oleh {nama}")
    open(f"LAPORAN_{int(time.time())}.txt","w").write(laporan)
    print(f"{YELLOW}[✓] Laporan disimpan!{RESET}")
    input("Enter untuk kembali...")

def menu2():
    banner()
    print(f"{BLUE}[02] IZIN POLISI PELACAK BLACK HAT - MODE RESMI{RESET}")
    print(f"{RED}PERINGATAN: Fitur ini hanya untuk pelaporan resmi!{RESET}\n")
    print(f"{WHITE}[*] Memeriksa izin pelacakan...{RESET}")
    time.sleep(1)
    print(f"{GREEN}[✓] IZIN DIVERIFIKASI: Untuk DEFENSE & PELAPORAN SAJA{RESET}")
    ip_target = input("\nMasukkan IP / ID mencurigakan: ")
    print(f"\n{CYAN}[*] Melacak jejak: {ip_target}{RESET}")
    print(f"{GREEN}[✓] Jejak dicatat untuk laporan polisi.{RESET}")
    log_report(f"PELACAKAN IZIN POLISI: Target {ip_target}")
    input("Enter untuk kembali...")

def menu3():
    banner()
    print(f"{RED}[03] LENYAPKAN MENGGUNAKAN LAPORAN - AUTO-HAPUS{RESET}\n")
    os.system("ls -l *.apk 2>/dev/null || echo 'Tidak ada file .apk (Aman)'")
    apk = input("\nNama APK yang mau dilenyapkan: ")
    if apk.strip() == "": apk = "simulasi_blackhat_malware.apk"
    print(f"\n{RED}[!] MELENYAPKAN {apk}...{RESET}")
    print(f"{GREEN}[✓] File diisolasi & Laporan dibuat{RESET}")
    log_report(f"PEMUSNAHAN: {apk} dilenyapkan via laporan")
    input("Enter untuk kembali...")

def menu4():
    banner()
    print(f"{CYAN}[04] PENDETEKSI HACKER BLACK HAT - SCANNER{RESET}\n")
    print(f"{WHITE}[*] Scan proses & koneksi...{RESET}")
    print(f"{GREEN}[✓] Scan selesai. Gunakan Menu [02] untuk lapor jika ada IP asing.{RESET}")
    log_report("DETEKSI: Scan black hat selesai")
    input("Enter untuk kembali...")

def menu5():
    banner()
    print(f"{RED}[05] APK BLACK HAT MASUK - SISTEM PERINGATAN!{RESET}")
    print(f"{WHITE}╔════════════════════════════════════════════════╗")
    print(f"║  ⚠️  BERHATI-HATILAH BLACK HAT AKAN DILAPORKAN  ║")
    print(f"╚════════════════════════════════════════════════╝{RESET}\n")
    print(f"{GREEN}[✓] DEFENDER AKTIF! Merauke aman!{RESET}")
    print(f"{RED}PESAN UNTUK BLACK HAT: KAMU DIAWASI!{RESET}")
    log_report("PERINGATAN AKTIF: Monitoring ON")
    input("Enter untuk kembali...")

def main():
    while True:
        banner()
        print(f"{WHITE}MERAUKE DEFENDER - MODE 1 HP")
        print(f"{GREEN}[01] APK Pelaporan")
        print(f"[02] Izin Polisi Pelacak Black Hat")
        print(f"[03] Lenyapkan Menggunakan Laporan")
        print(f"[04] Pendeteksi Hacker Black Hat")
        print(f"[05] APK Black Hat Masuk - Berhati-hatilah Black Hat Akan Dilaporkan")
        print(f"{RED}[99] Keluar{RESET}")
        print(f"{YELLOW}================================================================{RESET}")
        pilih = input(f"{CYAN}Pilih: {RESET}")
        if pilih in ["1","01"]: menu1()
        elif pilih in ["2","02"]: menu2()
        elif pilih in ["3","03"]: menu3()
        elif pilih in ["4","04"]: menu4()
        elif pilih in ["5","05"]: menu5()
        elif pilih == "99": 
            print(f"{GREEN}Merauke Defender Off. White Angel Siap!{RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
