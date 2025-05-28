import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import os

def tfidf_vektor_uret(csv_yolu, model_kayit_adi):
    df = pd.read_csv(csv_yolu)
    metinler = df.iloc[:, 0].astype(str)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(metinler)
    with open(f"{model_kayit_adi}.pkl", "wb") as f:
        pickle.dump(tfidf_matrix, f)
    print(f"✅ {model_kayit_adi}.pkl başarıyla oluşturuldu.")

os.makedirs("veriler", exist_ok=True)
tfidf_vektor_uret("veriler/lema_sonuclar.csv", "veriler/tfidf_lemmatized")
tfidf_vektor_uret("veriler/stem_sonuclar.csv", "veriler/tfidf_stemmed")
