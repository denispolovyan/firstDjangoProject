from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
	 
class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		fields = ['title', 'announcement','fullText','date']
  
		widgets = {
			'title': TextInput(attrs={
				'class': 'form__input',
				'placeholder': 'Title',
				'maxlength': '50',
			}),
   		'announcement': TextInput(attrs={
				'class': 'form__input',
				'placeholder': 'Announcement',
				'maxlength': '250',
			}),
      	'fullText': Textarea(attrs={
				'class': 'form__input form__textarea',
				'placeholder': 'More about topic',
				'maxlength': '500',
			}),
         'date': DateTimeInput(attrs={
				'class': 'form__input',
				'placeholder': 'Publication date',
				'maxlength': '20',
			}),
		}
