import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cosine_sim(v1, v2):
    return cosine_similarity([v1], [v2])[0][0]

def average_word_vectors(words, model):
    vectors = [model.wv[word] for word in words if word in model.wv]
    if len(vectors) == 0:
        return np.zeros(model.vector_size)
    return np.mean(vectors, axis=0)
