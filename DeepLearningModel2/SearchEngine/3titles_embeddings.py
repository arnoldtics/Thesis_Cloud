import pickle
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer

path = "../../DataCleaning/"
df = pd.read_csv(path + "Name_LastName_Title_Year.csv")

# All the titles must be in a list
titles = df["Title"].tolist()

# Neural Network for create embedding for all thesis titles 
# These are crucial for the pre-search phase
# It is a model for sentence similiarity
embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# If no interface is available change the show_progress_bar to False
titles_embeddings = embedder.encode(titles, convert_to_tensor=True, show_progress_bar=True)

# Save the variable of the titles to use many times
pickle.dump(titles_embeddings, open("titles_embeddings", "wb"))
