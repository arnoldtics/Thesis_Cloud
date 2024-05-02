import pandas as pd
import pickle
from gensim.models import Word2Vec

df = pd.read_csv("PreprocessTesis.zip")

# vector_size -> number of dimensions of words vector that Word2Vec will produce
# window -> number of words to take in consideration before and after the main word context
# min_count -> minimum frequency that a word must have to be taken in consideration
# sg -> algorithm for training. In this case sg=1 uses Skip-gram
model = Word2Vec(df["Vector"], vector_size=100, window=5, min_count=1, sg=1)

pickle.dump(model, open("model1", "wb"))