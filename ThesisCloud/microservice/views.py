from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import pandas as pd
import pickle
import spacy
import sys
import os

def thesis_cloud(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

df = pd.read_csv("../DeepLearningModel/PreprocessTesis.zip")
model = pickle.load(open("../DeepLearningModel/model1", "rb"))
nlp = spacy.load("es_core_news_sm")

'''sys.path.append("../DeepLearningModel/")
from Microservice_interface import preprocess_text, most_related_thesis, sending_results
sys.path.append("../ThesisCloud/ThesisCloud")'''

def microservice(request):
    if request.method == 'POST':
        query = request.POST.get('microservice')
        df_results = most_related_thesis(df, query, model)
        results = sending_results(df_results)
        return render(request, 'results.html', {'results':results})
    else: return redirect('Thesis_Cloud')