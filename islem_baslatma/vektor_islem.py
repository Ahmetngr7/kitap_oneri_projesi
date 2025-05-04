import subprocess

print("=== TF-IDF Vektörleştirme Başlatılıyor ===")
subprocess.run(["python", "code/vektor/tfidf_vektor.py"], check=True)

print("=== Word2Vec Eğitimi Başlatılıyor ===")
subprocess.run(["python", "code/vektor/word2vec_egitim.py"], check=True)

print("=== Tüm vektör işlemleri tamamlandı ===")
