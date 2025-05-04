# Kitap Özet Projesi

Bu proje, Project Gutenberg'den indirilen klasik kitapların metinleri üzerinde çeşitli doğal dil işleme (NLP) ve vektörleştirme işlemleri gerçekleştirir.
Kitap Özeti Projesi, kitap metinlerini analiz etmek ve bu metinlerden anlamlı özetler üretmek amacıyla geliştirilmiştir. Bu proje, aşağıdaki temel amaçlar için kullanılabilir:

Kitap özetleri oluşturmak:                              Kitapların ana temalarını ve önemli noktalarını kısa ve öz bir şekilde çıkartmak.

Veri analizi ve metin madenciliği:                       Kitap metinlerinden özet çıkarma işlemiyle ilgili metin madenciliği ve analiz yapılabilir.

Vektörleştirme ve doğal dil işleme (NLP) teknikleri:     Metinleri matematiksel temsillerle analiz etmek ve metinlerin birbirleriyle ilişkilerini keşfetmek için kullanılan algoritmalar (TF-IDF, Word2Vec).

Eğitim ve araştırma:                                      NLP ve metin madenciliği tekniklerini öğrenmek ve araştırmalar için verimli bir araç sağlamak.


Özellikler

Veri Temizleme:                Kitap verileri, boşluklar, özel karakterler ve gereksiz kelimelerden temizlenir.

Lemmatization & Stemming:      Kitap metinlerinden kök kelimeler çıkartılır. Bu sayede, kelimelerin kök hallerine dönüştürülerek daha verimli analiz yapılır.

Vektörleştirme:                TF-IDF ve Word2Vec gibi tekniklerle metinler sayısal verilere dönüştürülerek, metinlerin matematiksel temsilleri oluşturulur.

Model Eğitimi:                 Gensim gibi kütüphanelerle, Word2Vec modelleri eğitilerek kelimelerin vektörel temsilini elde edilir.

Zipf’s Law:                    Kitap metinlerinde kelime sıklıklarını inceleyerek Zipf Yasası üzerinden analizler yapılır.

Teknolojiler
Python 3.10+:                  Proje Python ile yazılmıştır ve Python 3.10 veya daha yeni sürümlerle uyumludur.

Pandas:                        Verilerin işlenmesi ve CSV dosyalarına kaydedilmesi için kullanılır.

NLTK:                          Doğal dil işleme ve metin analizi için kullanılır.

Gensim:                        Word2Vec gibi vektörleştirme algoritmalarını çalıştırmak için kullanılır.

Matplotlib:                    Verilerin görselleştirilmesi için kullanılır.



## Klasör Yapısı

```
kitap_ozet_projesi/
│
├── code/
│   ├── kaynak.py
│   ├── lema_stem_code/
│   │   ├── lema.py
│   │   └── stem.py
│   ├── zipf_code/
│   │   ├── zipf_lema.py
│   │   └── zipf_stem.py
│   └── vektor/
│       ├── tfidf_vektor.py
│       └── word2vec_egitim.py
│
├── islem_baslatma/
│   ├── lema_stem_islem.py
│   ├── zipf_islem.py
│   └── vektor_islem.py
│
├── ciktilar/
│   ├── csv_dosyalari/
│   │   ├── temizlenmis.csv
│   │   ├── lema_sonuclar.csv
│   │   ├── stem_sonuclar.csv
│   │   └── basarisiz_kitaplar.txt
│   ├── zipf_dosyaları/
│   │   ├── grafikler/
│   │   │   ├── zipf_lema_loglog.png
│   │   │   └── zipf_stem_loglog.png
│   │   └── log dosyaları
│   └── vektor/
│       ├── tfidf_lemmatized.csv
│       ├── tfidf_stemmed.csv
│       └── modeller/
│           └── *.model (Word2Vec modelleri)
│
└── README.md
```

## Çalıştırma Adımları

### 1. Temizleme + Lemmatizasyon + Stemming
```bash
python islem_baslatma/lema_stem_islem.py
```

### 2. Zipf Yasası Analizi
```bash
python islem_baslatma/zipf_islem.py
```

### 3. Vektörleştirme (TF-IDF + Word2Vec)
```bash
python islem_baslatma/vektor_islem.py

```

uyarı: duruma göre py -3.10 ya da -3.11 kullanılması gerekir 

  eğer öyle ise :  py -3.10 islem_baslatma/vektor_islem.py   şeklinde çalıştırabilirsiniz


### yapı
```
Veri Türü	Model Türü	Window	Vektör Boyutu	Toplam

Lemmatized	::

CBOW	                2	100	
Skip-gram	            2	100	
CBOW	                4	100	
Skip-gram	            4	100	
CBOW	                2	300	
Skip-gram	            2	300	
CBOW	                4	300	
Skip-gram	            4	300	            8 adet

Stemmed	   ::           Aynı yapı			8 adet

📁 Toplam: 8 lemmatized + 8 stemmed = 16 model


Her biri ciktilar/vektor/modeller/"lema ve stem" klasörüne .model uzantısıyla kaydedilir.

```


## Bağımlılıklar

Aşağıdaki kütüphanelerin kurulu olması gereklidir:  

uyarı: python sürümünüze uygun kütüphaneleri yükleyiniz py.13 versiyonu desteklemiyor

- `nltk`
- `pandas`
- `matplotlib`
- `requests`
- `scikit-learn`
- `gensim`

Kurmak için:
```bash
pip install -r requirements.txt
```

## Açıklama

- `code/` klasöründe analiz ve işleme kodları yer alır. tüm işlem yapan kodlar bu klasörde bulunur 
- `islem_baslatma/` klasörü, her şeyi sırasıyla çalıştırabileceğin betikleri içerir. ilk önce lema-stem işlemi yapınız
- `ciktilar/` klasörü tüm çıktı dosyalarını barındırır: CSV’ler, grafikler, loglar ve modeller.
