import pandas as pd
import spacy

PATH = "../DataCleaning/"

df = pd.read_csv("Author_Title_Link_Year.zip")
nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens

df["Vector"] = df["Title"].apply(preprocess_text)

df.to_csv("PreprocessTesis.csv", index=False)