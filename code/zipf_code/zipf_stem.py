import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os


# Klasör oluştur
os.makedirs("ciktilar/zipf_dosyaları/grafikler", exist_ok=True)

# Stem uygulanmış veriler için CSV dosyasını oku
df = pd.read_csv('ciktilar/csv_dosyalari/stem_sonuclar.csv')

kelime_sayaci = Counter()

# Satırları dolaşarak kelimeleri say
for _, satir in df.iterrows():
    try:
        satir_str = satir["stem"]
        kelimeler = satir_str.split()
        kelime_sayaci.update(kelimeler)
    except Exception as e:
        print("Hatalı satır atlandı:", e)
        print("Satır Verisi:", satir_str)

# En yaygın 100 kelimeyi al
en_yaygin = kelime_sayaci.most_common(100)

if not en_yaygin:
    print("En yaygın 100 kelime alınamadı.")
else:
    kelimeler, frekanslar = zip(*en_yaygin)
    plt.figure(figsize=(14, 6))
    plt.plot(range(1, len(frekanslar)+1), frekanslar, marker='o')
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("Kelime Sırası (Rank)")
    plt.ylabel("Frekans")
    plt.title("Zipf Yasası - Stem Edilmiş Veri")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ciktilar/zipf_dosyaları/grafikler/zipf_stem_loglog.png")
    plt.close()
