import time, os
GREEN = "\033[92m"
BOLD_GREEN = "\033[1;92m"
RESET = "\033[0m"
NAGA = f"""{GREEN}
      ,     ,_
      |\\___/|
      | o o |  Naga Linux Hijau
      (  V  )
      /--m-m-
{RESET}"""
print(NAGA)
print(f"{BOLD_GREEN}WHITE ANGEL CHAT HIJAU AKTIF 🐉💚{RESET}")
while True:
    msg = input(f"{GREEN}Kamu: {RESET}")
    if msg == "exit": break
    print(f"{BOLD_GREEN}Naga 🐉: Pesan '{msg}' diamankan!{RESET}")
