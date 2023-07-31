from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('shop', views.shop, name="shop"),
    path('track', views.track, name="track"),
]
