from django.shortcuts import render
from .models import Articles

def newsHome(request):
   news = Articles.objects.order_by('-date')
   return render(request, 'news/newsHome.html', {'news': news})
