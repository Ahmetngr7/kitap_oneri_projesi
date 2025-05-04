import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os

def tfidf_uygula(dosya_yolu, kolon_adi, cikti_adi):
    df = pd.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", dosya_yolu)))
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df[kolon_adi])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

    print("CSV ciktilar klasörüne kaydediliyor:", os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "ciktilar", cikti_adi)
    ))
    tfidf_df.to_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "ciktilar", cikti_adi)), index=False)

os.makedirs(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "ciktilar")), exist_ok=True)

tfidf_uygula("ciktilar/csv_dosyalari/lema_sonuclar.csv", "lema", "tfidf_lemmatized.csv")
tfidf_uygula("ciktilar/csv_dosyalari/stem_sonuclar.csv", "stem", "tfidf_stemmed.csv")
