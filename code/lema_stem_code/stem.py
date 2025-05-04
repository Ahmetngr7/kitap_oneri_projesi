import pandas as pd
from nltk.stem import PorterStemmer
import nltk

# Gerekli NLTK veri setini indiriyoruz (tokenization için)
nltk.download('punkt')

# CSV dosyasını okuyoruz
df = pd.read_csv("ciktilar/csv_dosyalari/temizlenmis.csv")

# Stemming nesnesi oluşturuyoruz
stemmer = PorterStemmer()

# "temiz_metin" sütunundaki metinleri stem ediyoruz
df["stem"] = df["temiz_metin"].apply(lambda text: ' '.join([stemmer.stem(w) for w in text.split()]))

# Yeni verileri dosyaya yazıyoruz
df[["kitap", "stem"]].to_csv("ciktilar/csv_dosyalari/stem_sonuclar.csv", index=False)
