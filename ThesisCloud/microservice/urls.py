from django.urls import path
from . import views

urlpatterns = [
    path('', views.thesis_cloud, name='Thesis_Cloud'),
]