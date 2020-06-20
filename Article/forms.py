from django.forms import ModelForm
from django import forms
import datetime
from Article.models import Author, Book

class Comment(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' = ', help_text='Full')
    email = forms.EmailField(label='Email', required=False, initial='www.')
    date = forms.DateField(initial=datetime.date.today)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']