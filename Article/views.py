from django.shortcuts import render
from Article.forms import AuthorForm, BookForm
from django.http import HttpResponse
def view(request):
    if (request.method=='GET'):
        author_form = AuthorForm()
        book_form = BookForm()
        print(author_form)

        return render(request, 'article.html', {'author_form':author_form,'book_form':book_form})
    else:
        author_form_post = AuthorForm(request.POST)
        print(author_form_post.is_valid())
        if (author_form_post.is_valid()):
            author_form_post.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Failure')
# Create your views here.
