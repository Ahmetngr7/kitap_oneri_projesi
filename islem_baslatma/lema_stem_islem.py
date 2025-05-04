import os
import subprocess

print("1. Kaynak veriler indiriliyor ve temizleniyor...")
subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "code", "kaynak.py"))], check=True)

print("2. Lemmatizasyon uygulanıyor...")
subprocess.run(["python", "code/lema_stem_code/lema.py"], check=True)

print("3. Stemming uygulanıyor...")
subprocess.run(["python", "code/lema_stem_code/stem.py"], check=True)

print("✅ Tüm işlemler tamamlandı. Çıktılar csv_dosyalari klasöründe.")
