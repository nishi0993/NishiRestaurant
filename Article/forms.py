from django.forms import ModelForm
from django import forms
from Article.models import Author, Book

class Comment(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Email', required=False)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']