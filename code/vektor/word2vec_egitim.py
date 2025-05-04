
import pandas as pd
from gensim.models import Word2Vec
import os

parameters = [
    {'model_type': 'cbow', 'window': 2, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 2, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 300},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 300},
]

def egit(dosya, kolon, veri_tipi):
    df = pd.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", dosya)))
    corpus = [str(metin).split() for metin in df[kolon].fillna("")]
    for p in parameters:
        sg = 0 if p["model_type"] == "cbow" else 1
        model = Word2Vec(
            sentences=corpus,
            vector_size=p["vector_size"],
            window=p["window"],
            sg=sg,
            min_count=1,
            workers=2,
            epochs=100
        )
        # hedef klasörü lemmatized ve stemmed olarak ayır
        alt_klasor = "lema" if veri_tipi == "lemmatized" else "stem"
        model_adi = f"word2vec_{veri_tipi}_{p['model_type']}_win{p['window']}_dim{p['vector_size']}.model"
        model_yolu = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "..", "ciktilar", "vektor", "modeller", alt_klasor, model_adi
        ))
        os.makedirs(os.path.dirname(model_yolu), exist_ok=True)
        print("Model kaydediliyor:", model_yolu)
        model.save(model_yolu)

# Eğitim
egit("ciktilar/csv_dosyalari/lema_sonuclar.csv", "lema", "lemmatized")
egit("ciktilar/csv_dosyalari/stem_sonuclar.csv", "stem", "stemmed")
