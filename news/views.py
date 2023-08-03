from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def newsHome(request):
   news = Articles.objects.order_by('-date')
   return render(request, 'news/newsHome.html', {'news': news})


class NewsDetailViews(DetailView):
   model = Articles
   template_name = 'news/newsDetailViews.html'
   context_object_name = 'article'

class NewsUpdateViews(UpdateView):
   model = Articles
   template_name = 'news/newsCreate.html'
   form_class = ArticlesForm
   
   
class NewsDeleteViews(DeleteView):
   model = Articles
   template_name = 'news/newsDelete.html'
   success_url = '/news/'
   context_object_name = 'article'
   
   
      
def newsCreate(request):
   error = ''
   
   if request.method == 'POST':
      form = ArticlesForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('newsHome')
      else:
         error = 'Form was wrong'
         
         
   
   form = ArticlesForm()
   data = {
		'form': form,
		'error': error,
	}
   return render(request, 'news/newsCreate.html', data)