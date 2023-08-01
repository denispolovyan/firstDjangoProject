from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsHome, name="newsHome"),
    path('create', views.newsCreate, name="newsCreate"),
]
