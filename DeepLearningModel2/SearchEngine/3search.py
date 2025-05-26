import pickle
import pandas as pd
import torch
from torch.nn.functional import cosine_similarity
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sentence_transformers import SentenceTransformer

# PRESEARCH
def presearch(query:str):
    # Loading the embeddings 
    titles_embeddings = pickle.load(open("titles_embeddings", "rb")) 
    titles_embeddings = titles_embeddings.to("cuda")

    # Loading neural network to do the pre-search. Must be the same model that was used for the titles embeddings
    embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

    # Creating the query embedding
    query_embedding = embedder.encode(query, convert_to_tensor=True).to(embedder.device.type) 

    # Calculating the distances between the titles and the query using cosine similarity
    cosine_scores = torch.nn.functional.cosine_similarity(query_embedding, titles_embeddings)

    # Getting the k best results for the rerank process
    k = 1000 # Adjust value of k results of the presearch
    top_results = torch.topk(cosine_scores, k)

    return top_results

# SEARCH
def search(query, top_results):
    path = "../../DataCleaning/"
    df = pd.read_csv(path + "Name_LastName_Title_Year.csv")

    # All the titles must be in a list
    titles = df["Title"].tolist()

    # Loading neural network to do the search.
    # It is a model for text-ranking
    tokenizer = AutoTokenizer.from_pretrained("Alibaba-NLP/gte-multilingual-reranker-base")
    model = AutoModelForSequenceClassification.from_pretrained(
        "Alibaba-NLP/gte-multilingual-reranker-base",
        trust_remote_code = True,
        torch_dtype = torch.float16
    )
    model.eval()
    model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    # In text-ranking couples {document, query} must be created
    couples = [[titles[i], query] for i in top_results.indices]

    # MAIN PART
    with torch.no_grad():
        # Tokenize candidates
        inputs = tokenizer(couples, padding=True, truncation=True, return_tensors='pt', max_length=512)
        inputs = {k: v.to(torch.device("cuda" if torch.cuda.is_available() else "cpu")) for k, v in inputs.items()}
        # Getting the tensor scores. Bigger values mean more similarity
        scores = model(**inputs, return_dict=True).logits.view(-1, ).float()

    # Getting the final recomendation: 10 thesis 
    final = torch.topk(scores, k=10)
    thesis = [couples[i][0] for i in final.indices]

    return thesis
    