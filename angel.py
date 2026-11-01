import requests

url = "http://testphp.vulnweb.com"

payloads = [
    "/redirect?url=https://google.com",
    "/?next=https://google.com",
    "/?redirect=https://evil.com"
]

print("[WHITE ANGEL] Berburu Open Redirect...")
for p in payloads:
    try:
        full = url + p
        r = requests.get(full, allow_redirects=False, timeout=3)
        if r.status_code in [301, 302] and "google.com" in r.headers.get("Location",""):
            print(f"[JACKPOT $50!] Nemu di: {full}")
        else:
            print(f"[Aman] {full} -> {r.status_code}")
    except:
        print(f"[Kabur] {full}")
import requests

url = "http://testphp.vulnweb.com"

payloads = [
    "/redirect?url=https://google.com",
    "/?next=https://google.com",
    "/?redirect=https://evil.com"
]

print("[WHITE ANGEL] Berburu Open Redirect...")
for p in payloads:
    try:
        full = url + p
        r = requests.get(full, allow_redirects=False, timeout=3)
        if r.status_code in [301, 302] and "google.com" in r.headers.get("Location",""):
            print(f"[JACKPOT $50!] Nemu di: {full}")
        else:
            print(f"[Aman] {full} -> {r.status_code}")
    except:
        print(f"[Kabur] {full}")
0

