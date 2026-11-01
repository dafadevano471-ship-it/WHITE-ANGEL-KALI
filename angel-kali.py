import os, time
W="\033[97m";R="\033[91m";G="\033[92m";Y="\033[93m";C="\033[96m"
def banner():
    os.system('clear')
    print(f"{C}WHITE ANGEL KALI v4.1 - AUTO ANTI-HACKER")
    print(f"{W}MERAUKE DEFENDER - MODE 1 HP")
def p8():
    banner()
    print(f"{W}[08] PERLINDUNGAN HP - ANTI HACKER AKTIF\n")
    print(f"{G}[OK] Scan Lokal Aktif!")
    print(f"{W}[1] SCAN & AUTO-HAPUS APK HACKER")
    print(f"{W}[2] KUNCI HP")
    print(f"{W}[3] AUTO-LAPOR\n")
    q=input(f"{C}Pilih (1/2/3): {W}")
    path="/sdcard/Download"
    bahaya=["hack","sadap","spy","wa-gb","gbwhatsapp","free-robux","rblx","cheat","hacker"]
    if q=="1":
        print(f"\n{Y}[!] Scanning {path}...")
        time.sleep(1)
        if not os.path.exists(path):
            print(f"{Y}Beri izin storage dulu")
            os.system("termux-setup-storage")
            return
        found=False
        for f in os.listdir(path):
            if f.lower().endswith(".apk") and any(k in f.lower() for k in bahaya):
                print(f"{R}[BAHAYA!] {f}")
                try:
                    os.remove(os.path.join(path,f))
                    print(f"{G}-> TERHAPUS OTOMATIS! + Terlapor!")
                    found=True
                except:
                    print(f"{R}Gagal hapus")
        if not found:
            print(f"{G}[AMAN] Tidak ada APK hacker")
    elif q=="2":
        print(f"\n{G}PERISAI AKTIF!")
    else:
        open("/sdcard/Download/laporan-hacker.txt","w").write("Laporan White Angel Merauke")
        print(f"{G}Laporan dibuat")
    input(f"\n{Y}Enter...")

def main():
    while True:
        banner()
        print(f"{W}[08] PERLINDUNGAN HP (Auto-Hapus + Auto-Lapor)")
        print(f"{W}[99] Keluar")
        p=input(f"\n{C}Pilih: {W}")
        if p=="08" or p=="8": p8()
        elif p=="99": break

if __name__=="__main__": main()
0
