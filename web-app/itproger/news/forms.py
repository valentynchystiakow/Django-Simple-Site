# import models
from .models import Articles
# import libraries(modules)
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


# Articles form
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcement', 'full_text', 'date']
        # ads attributes to poles of the form
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),
            "announcement": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication date'
            })

        }



