import pandas as pd
from nltk.stem import WordNetLemmatizer
import nltk

# Gerekli NLTK kaynaklarını indiriyoruz
nltk.download('wordnet')

# CSV dosyasını okuyoruz
df = pd.read_csv("ciktilar/csv_dosyalari/temizlenmis.csv")

# Lemmatizer nesnesi oluşturuyoruz
lemmatizer = WordNetLemmatizer()

# "temiz_metin" sütunundaki metinleri lemmatize ediyoruz
df["lema"] = df["temiz_metin"].apply(lambda text: ' '.join([lemmatizer.lemmatize(w) for w in text.split()]))

# Yeni verileri dosyaya yazıyoruz
df[["kitap", "lema"]].to_csv("ciktilar/csv_dosyalari/lema_sonuclar.csv", index=False)
