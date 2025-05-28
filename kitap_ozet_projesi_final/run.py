import os

print("🔁 TF-IDF vektörleri oluşturuluyor...")
os.system("python tfidf_olustur.py")

print("\n🧪 Util modülü içe aktarımı:")
try:
    from util import cosine_sim, average_word_vectors
    print("✅ util.py başarıyla içe aktarıldı.")
except Exception as e:
    print(f"❌ util.py içe aktarılamadı: {e}")

print("\n📊 Benzerlik analizi başlatılıyor...")
os.system("python benzerlik_hesapla.py")
