import pandas as pd
import pickle
import spacy

df = pd.read_csv("PreprocessTesis.zip")
model = pickle.load(open("model1", "rb"))
nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens

def most_related_tesis(dataframe, new_title, model):
    jacard = []
    vector = model.wv[preprocess_text(new_title)]
    similarTitles = model.wv.most_similar(positive=vector, topn=10)
    words = [word.lower() for word, prob in similarTitles]
    for i, title in enumerate(dataframe["Vector"]):
        title, count = title[1:-1].strip().lower().replace("'", "").split(", "), 0
        for word in words:
            for context in title: 
                if word == context: count += 1
        jacard.append((count, i))
    jacard.sort()
    results = reversed([i for jac, i in jacard[-10:]])
    return dataframe.loc[results]

def sending_results(dataframe):
    results = {}
    for i in dataframe.index:
        title = dataframe.loc[i]["Title"]
        author = dataframe.loc[i]["Name"]
        year = dataframe.loc[i]["Year"]
        link = dataframe.loc[i]["Link"]
        results[i] = {"title": title, "author": author, "year": year, "link": link}
    return results
