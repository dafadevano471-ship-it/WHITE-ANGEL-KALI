print("🐉 Naga Linux cek password...")
pwd = input("Masukin password buat dicek (password kamu sendiri ya): ")

skor = 0
if len(pwd) >= 8: skor += 1
if any(c.isupper() for c in pwd): skor += 1
if any(c.islower() for c in pwd): skor += 1
if any(c.isdigit() for c in pwd): skor += 1
if any(c in "!@#$%^&*" for c in pwd): skor += 1

print("\n--- HASIL NAGA ---")
if skor <= 2:
    print(f"💀 BAHAYA! Skor {skor}/5 - Gampang dibobol!")
    print("Saran naga: Ganti yang panjang + ada huruf besar + angka + simbol")
elif skor == 3:
    print(f"⚠️ LUMAYAN Skor {skor}/5 - Masih bisa dibobol")
else:
    print(f"🛡️ AMAN! Skor {skor}/5 - Hacker susah bobol")

# simulasi waktu bobol
if len(pwd) < 6:
    print("Waktu bobol: < 1 detik 😱")
elif len(pwd) < 8:
    print("Waktu bobol: 5 menit")
else:
    print("Waktu bobol: 100 tahun+ (naga jaga)")
