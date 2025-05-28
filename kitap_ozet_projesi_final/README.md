# Kitap Özet Projesi – Metin Benzerliği

Bu proje, TF-IDF ve Word2Vec modelleri ile kitap özetleri arasında benzerlikleri hesaplar.

modellerin yarısı yüklenmiştir (boyut nedeni ile)

## Gerekli Dosyalar

- `veriler/` klasöründe:
  - `lema_sonuclar.csv`
  - `stem_sonuclar.csv`
  - 16 adet `.model` dosyası (Word2Vec)
  - Çalışınca oluşturulan `.pkl` dosyaları

## Kullanım

```bash
pip install -r requirements.txt
python run.py
```

## Açıklama

- `run.py`: Tüm işlemleri sırayla çalıştırır
- `tfidf_olustur.py`: CSV'den TF-IDF `.pkl` dosyası üretir
- `benzerlik_hesapla.py`: Benzerlik analizi yapar
- `util.py`: Yardımcı fonksiyonlar içerir
