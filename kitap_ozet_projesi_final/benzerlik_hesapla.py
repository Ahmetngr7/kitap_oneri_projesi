import pandas as pd
import numpy as np
import pickle
import os
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from util import cosine_sim, average_word_vectors

def tfidf_benzerlik(giris_index, metinler, tfidf_matrix, model_adi):
    giris_vector = tfidf_matrix[giris_index]
    skorlar = cosine_similarity(giris_vector, tfidf_matrix)[0]
    ilk5 = np.argsort(skorlar)[::-1][1:6]
    print(f"\n{model_adi} için en benzer 5 metin:")
    for i in ilk5:
        print(f"{i}. Skor: {skorlar[i]:.4f} -> {metinler[i]}")
    return ilk5

def word2vec_benzerlik(giris_index, metinler, model_path):
    model = Word2Vec.load(model_path)
    giris_cumle = metinler[giris_index].lower().split()
    print(f"\n[DEBUG] Giriş cümlesi kelimeleri: {giris_cumle}")
    for k in giris_cumle:
        print(f"[DEBUG] '{k}' modelde {'VAR' if k in model.wv else 'yok'}")

    giris_v = average_word_vectors(giris_cumle, model)

    skorlar = []
    for cumle in metinler:
        v = average_word_vectors(cumle.lower().split(), model)
        skorlar.append(cosine_sim(giris_v, v))

    skorlar = np.array(skorlar)
    ilk5 = np.argsort(skorlar)[::-1][1:6]
    print(f"\n{os.path.basename(model_path)} için en benzer 5 metin:")
    for i in ilk5:
        print(f"{i}. Skor: {skorlar[i]:.4f} -> {metinler[i]}")
    return ilk5

def main():
    base_dir = 'veriler'
    giris_index = 81  # "The Prince and the Pauper" örneği için

    for tfidf_file, metin_file, ad in [
        ("tfidf_lemmatized.pkl", "lema_sonuclar.csv", "TF-IDF Lemmatized"),
        ("tfidf_stemmed.pkl", "stem_sonuclar.csv", "TF-IDF Stemmed")
    ]:
        with open(os.path.join(base_dir, tfidf_file), 'rb') as f:
            tfidf = pickle.load(f)
        metinler = pd.read_csv(os.path.join(base_dir, metin_file)).iloc[:, 0].astype(str).tolist()
        tfidf_benzerlik(giris_index, metinler, tfidf, ad)

    for model_file in os.listdir(base_dir):
        if model_file.endswith(".model"):
            model_path = os.path.join(base_dir, model_file)
            metin_dosya = "lema_sonuclar.csv" if "lemmatized" in model_file else "stem_sonuclar.csv"
            metinler = pd.read_csv(os.path.join(base_dir, metin_dosya)).iloc[:, 0].astype(str).tolist()
            word2vec_benzerlik(giris_index, metinler, model_path)

if __name__ == "__main__":
    main()
