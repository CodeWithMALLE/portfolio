from django import forms
from .models import Articles


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Articles
		fields = ("titre", "categorie", "content", "img")
		widgets = {
			'content': forms.Textarea(attrs={'class': 'content'})
		}

