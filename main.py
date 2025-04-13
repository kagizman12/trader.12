# main.py

from config import SYMBOLS
from volume_analyzer import analyze_volume

print("📈 Borsa İstanbul Hacim Analizi Başladı...\n")

for symbol in SYMBOLS:
    result = analyze_volume(symbol)
    print(result)
