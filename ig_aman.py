import random, string, os, time
os.system('clear')
print("🔒 WHITE ANGEL - IG SHIELD SYSTEM 🔒\n")

# Generate password super kuat
def buat_password_kuat():
    huruf = string.ascii_letters
    angka = string.digits
    simbol = "!@#$%^&*"
    semua = huruf + angka + simbol
    pwd = ''.join(random.choice(semua) for _ in range(16))
    return pwd

print("[1] PASSWORD KAMU SEKARANG AMAN ATAU TIDAK?")
print("Ciri password LEMAH yang gampang dibobol hacker:")
print(" - pakai nama, tanggal lahir, 12345, password")
print(" - pendek kurang dari 12 huruf")
print(" - sama untuk IG, FB, Game\n")

time.sleep(1)
print("[2] INI CONTOH PASSWORD KUAT BUATAN NAGA IJO 🐉:")
for i in range(3):
    print(f" -> {buat_password_kuat()}")

print("\n[3] CHECKLIST IG ANTI-HACKER WAJIB:")
print(" [ ] 1. Aktifkan 2FA / Two-Factor (paling penting!)")
print(" [ ] 2. Email IG harus email yang aktif & aman")
print(" [ ] 3. No HP sudah terpasang di IG")
print(" [ ] 4. Jangan klik link 'dapet centang biru gratis'")
print(" [ ] 5. Jangan login IG di web aneh selain instagram.com")
print(" [ ] 6. Password beda dengan game & lainnya")

print("\n[4] CARA AKTIFKAN 2FA SEKARANG:")
print(" Buka IG > Profil > Garis 3 > Pusat Akun >")
print(" Kata Sandi dan Keamanan > Autentikasi Dua Faktor >")
print(" Pilih SMS atau Aplikasi Autentikasi > AKTIFKAN")

print("\n" + "="*45)
print(" IG KAMU 99% AMAN KALO 2FA AKTIF!")
print("="*45)
