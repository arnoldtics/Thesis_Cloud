from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from Microservice_interface import most_related_thesis, sending_results
import pandas as pd
import pickle

df = pd.read_csv("../DeepLearningModel/PreprocessTesis.zip")
model = pickle.load(open("../DeepLearningModel/model1", "rb"))

def microservice(request):
    if request.method == 'GET':
        query = request.GET['microservice']
        try:
            df_results = most_related_thesis(df, query, model)
            results = sending_results(df_results)
            return render(request, 'results.html', {"results":results})
        except: 
            messages.error(request, "Sorry for the inconvenience, our deep learning model has not been train for your query.")
            return redirect('Thesis_Cloud')
    else: return redirect('Thesis_Cloud')

def thesis_cloud(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())