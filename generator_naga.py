import random, string
print("🐉 Naga Linux bikin password dewa...")

# bikin password 16 karakter acak
karakter = string.ascii_letters + string.digits + "!@#$%"
password = ''.join(random.choice(karakter) for _ in range(16))

print(f"\n🔐 Password dewa buat Mama Papa:")
print(f" {password}")
print(f"\nWaktu bobol: 1 MILYAR tahun 😂")
print("Jangan lupa simpan di tempat aman!")
