#!/bin/bash
# White Angel - Merauke, Papua - Bug Bounty Tool v1.0
# Scanner Open Redirect - Legal & Ethical Only!

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}"
echo " __      __  _     _  _           ___                _ "
echo " \\ \\ /\\ / / | |__ (_) |_  ___  / _ \\  /\\  \\ | | ___ "
echo "  \\ V  V /  | '_ \\| | __|/ _ \\/ /_\\ \\/ /\\/ / | |/ _ \\"
echo "   \\_/\\_/   | | | | | |_|  __/ /__\\\\  /   /  | | (_) |"
echo "           |_| |_|_|\\__|\\___\\__/   \\/    |_|\\___/ "
echo -e "${NC}"
echo "  White Angel - Merauke, Papua - Bug Hunter"
echo "  Tool: Open Redirect Scanner"
echo "------------------------------------------"

if [ -z "$1" ]; then
  echo "Cara pakai: ./white_angel.sh https://target.com/redirect?url="
  exit 1
fi

TARGET=$1
PAYLOAD="https://evil.com"
URL="${TARGET}${PAYLOAD}"

echo "[*] Testing: $URL"
echo "[*] Tunggu 5 detik..."

RESPONSE=$(curl -m 10 -s -I "$URL")

if echo "$RESPONSE" | grep -qi "location:.*evil.com"; then
  echo -e "${GREEN}[+] BUG KETEMU BOSS! Open Redirect VULNERABLE!${NC}"
  echo "$RESPONSE" | grep -i location
  echo ""
  echo "BUKTI BUG:" > laporan_white_angel.txt
  echo "URL: $URL" >> laporan_white_angel.txt
  echo "$RESPONSE" | grep -i location >> laporan_white_angel.txt
  echo "Found by White Angel - Merauke" >> laporan_white_angel.txt
  echo "[*] Laporan disimpan di laporan_white_angel.txt"
else
  echo -e "${RED}[-] Aman, tidak vulnerable${NC}"
  echo "$RESPONSE" | head -5
fi
0

