import gensim.downloader as api
from gensim.models import Word2Vec

corpus=api.load("text8")
api.info("text8")

model=Word2Vec(corpus)
print(model)