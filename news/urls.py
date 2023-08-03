from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsHome, name="newsHome"),
    path('create', views.newsCreate, name="newsCreate"),
    path('<int:pk>', views.NewsDetailViews.as_view(), name="newsDetail"),
    path('<int:pk>/update', views.NewsUpdateViews.as_view(), name="newsUpdate"),
    path('<int:pk>/delete', views.NewsDeleteViews.as_view(), name="newsDelete"),
    
]
