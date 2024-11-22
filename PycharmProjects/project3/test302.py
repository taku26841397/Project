import gensim.downloader as api
from gensim.models import Word2Vec


corpus= api.load("text8")
model=Word2Vec(corpus)

simililarity_words=model.wv.most_similar("japan")
print(simililarity_words)

