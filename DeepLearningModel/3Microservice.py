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

def most_related_thesis(dataframe, new_title, model):
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

def presenting_results(dataframe):
    for i in dataframe.index:
        print(f"\nTítle: {dataframe.loc[i]["Title"]}")
        print(f"Author: {dataframe.loc[i]["Name"]}")
        print(f"Year: {dataframe.loc[i]["Year"]}")
        print(f"Link: {dataframe.loc[i]["Link"]}")

if __name__ == "__main__":
    title = input("Write the new thesis title:\n").strip()
    df_results = most_related_thesis(df, title, model)
    print("The ten most related theses are:")
    presenting_results(df_results)