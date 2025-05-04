import os
import requests
import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

nltk.download('punkt')
nltk.download('stopwords')

def oturum_olustur():
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def gutenberg_kitap_indir(gutenberg_id, session):
    url1 = f"https://www.gutenberg.org/files/{gutenberg_id}/{gutenberg_id}-0.txt"
    url2 = f"https://www.gutenberg.org/cache/epub/{gutenberg_id}/pg{gutenberg_id}.txt"
    for url in [url1, url2]:
        try:
            response = session.get(url, timeout=15)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"Hata: {e}")
            continue
    return None

# Temizleme işlemi
def metin_temizle(metin):
    # Küçük harfe dönüştür
    metin = metin.lower()
    
    # Noktalama işaretlerini kaldır
    metin = ''.join(c for c in metin if c not in string.punctuation)
    
    # Nümerik karakterler ve özel karakterlerden arındırma
    metin = ''.join(c for c in metin if c.isalpha() or c.isspace())
    
    # Tokenize et ve stopwords (gereksiz kelimeler) kaldır
    kelimeler = word_tokenize(metin)
    kelimeler = [k for k in kelimeler if k not in stopwords.words('english')]
    
    return kelimeler

# Özet çıkarma fonksiyonu
def ozet_cikar(metin, cumle_sayisi=5):
    cumleler = sent_tokenize(metin)
    return " ".join(cumleler[:cumle_sayisi])

# Kitap listesi
kitaplar = {
    "Pride and Prejudice": 1342,
    "Moby-Dick": 2701,
    "War and Peace": 2600,
    "Hamlet": 1524,
    "The Odyssey": 1727,
    "Crime and Punishment": 2554,
    "Wuthering Heights": 768,
    "The Divine Comedy": 8800,
    "Frankenstein": 84,
    "Dracula": 345,
    "The Picture of Dorian Gray": 174,
    "The Iliad": 6130,
    "A Tale of Two Cities": 98,
    "Heart of Darkness": 219,
    "The Count of Monte Cristo": 1184,
    "Treasure Island": 120,
    "The Scarlet Letter": 33,
    "The Adventures of Tom Sawyer": 74,
    "Gulliver's Travels": 829,
    "The Jungle Book": 236,
    "Peter Pan": 16,
    "Around the World in 80 Days": 103,
    "The Time Machine": 35,
    "The Call of the Wild": 215,
    "The Prince": 1232,
    "The Adventures of Sherlock Holmes": 1661,
    "Little Women": 514,
    "The Wonderful Wizard of Oz": 55,
    "Oliver Twist": 730,
    "Les Misérables": 135,
    "Don Quixote (Çeviri)": 996,
    "The Secret Garden": 113,
    "Persuasion": 105,
    "Sense and Sensibility": 161,
    "Northanger Abbey": 121,
    "Emma": 158,
    "The Souls of Black Folk": 408,
    "The Turn of the Screw": 209,
    "The War of the Worlds": 36,
    "The Wind in the Willows": 27805,
    "The Hound of the Baskervilles": 2852,
    "The Man Who Was Thursday": 1695,
    "A Christmas Carol": 46,
    "Dr. Jekyll and Mr. Hyde": 43,
    "The Thirty-Nine Steps": 558,
    "The Metamorphosis": 5200,
    "Ethan Frome": 4517,
    "The Legend of Sleepy Hollow": 2048,
    "The Yellow Wallpaper": 1952,
    "The Man in the Iron Mask": 2759,
    "Memoirs of Sherlock Holmes": 834,
    "Return of Sherlock Holmes": 221,
    "A Study in Scarlet": 244,
    "The Valley of Fear": 3289,
    "A Princess of Mars": 62,
    "At the Earth’s Core": 552,
    "Tarzan of the Apes": 78,
    "The Lost World": 139,
    "The Island of Doctor Moreau": 159,
    "The Invisible Man": 5230,
    "The House of Mirth": 284,
    "The Age of Innocence": 421,
    "The Awakening": 160,
    "The Secret Agent": 974,
    "The Brothers Karamazov": 28054,
    "Notes from the Underground": 600,
    "Thus Spoke Zarathustra": 1998,
    "Beyond Good and Evil": 4363,
    "The Social Contract": 46333,
    "Candide": 19942,
    "The Federalist Papers": 1404,
    "Common Sense": 147,
    "Democracy in America": 815,
    "Narrative of the Life of Frederick Douglass": 23,
    "Confessions of St. Augustine": 3296,
    "The Republic": 1497,
    "Meditations": 2680,
    "Walden": 205,
    "On the Origin of Species": 2009,
    "The Communist Manifesto": 61,
    "The Wealth of Nations": 363,
    "The Prince and the Pauper": 2611,
    "Gitanjali": 30376,
    "The Tempest": 2200,
    "A Room of One’s Own": 1760,
    "The Canterbury Tales": 21136,
    "The Power of the Dog": 15765,
    "The Aeneid": 1212,
    "The Complete Works of William Shakespeare": 10000,
    "The Art of War": 1338,
    "The Old Man and the Sea": 1697,
    "The Trial": 1743,
    "The Plague": 2812,
    "The House of the Seven Gables": 141,
    "The Scarlet Pimpernel": 1733,
    "The Murder of Roger Ackroyd": 1681,
    "The Three Musketeers": 7161,
    "Dracula's Guest": 34245,
    "A Connecticut Yankee in King Arthur's Court": 86,
}

kitaplar_temiz = []
basarisizlar = []


# HTTP oturumu oluştur
session = oturum_olustur()

# Kitapları indir ve işleme
for isim, gid in kitaplar.items():
    print(f"İndiriliyor: {isim} ({gid})")
    metin = gutenberg_kitap_indir(gid, session)
    if metin:
        try:
            ozet = ozet_cikar(metin)
            temiz = metin_temizle(ozet)
            kitaplar_temiz.append({"kitap": isim, "temiz_metin": ' '.join(temiz)})
        except Exception as e:
            print(f"İşlenemedi: {isim} -> {e}")
            basarisizlar.append(f"{isim} ({gid}) - İşleme hatası: {e}")
    else:
        print(f"İndirilemedi: {isim} ({gid})")
        basarisizlar.append(f"{isim} ({gid}) - İndirme hatası")

# Veriyi CSV'ye yaz
try:
    pd.DataFrame(kitaplar_temiz).to_csv("ciktilar/csv_dosyalari/temizlenmis.csv", index=False, encoding="utf-8")
    print("CSV dosyası başarıyla kaydedildi.")
except Exception as e:
    print(f"CSV kaydetme hatası: {e}")

# Başarısızları txt dosyasına yaz
try:
    with open("ciktilar/csv_dosyalari/basarisiz_kitaplar.txt", "w", encoding="utf-8") as f:
        for satir in basarisizlar:
            f.write(satir + "\n")
    print("Başarısız kitaplar dosyası başarıyla kaydedildi.")
except Exception as e:
    print(f"Başarısız kitaplar kaydetme hatası: {e}")
