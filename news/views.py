from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def newsHome(request):
   news = Articles.objects.order_by('-date')
   return render(request, 'news/newsHome.html', {'news': news})

def newsCreate(request):
   error = ''
   
   if request.method == 'POST':
      form = ArticlesForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home')
      else:
         error = 'Form was wrong'
         
         
   
   form = ArticlesForm()
   data = {
		'form': form,
		'error': error
	}
   return render(request, 'news/newsCreate.html', data)