from django.shortcuts import render
from Article.forms import AuthorForm, BookForm, Comment
from django.http import HttpResponse

def formview(request):
    comment = Comment()
    print(comment)
    return render(request, 'article.html',{'comment':comment})

def view(request):
    if (request.method=='GET'):
        author_form = AuthorForm()
        book_form = BookForm()
        # print(author_form)

        return render(request, 'article.html', {'author_form':author_form,'book_form':book_form})
    else:
        author_form_post = AuthorForm(request.POST)
        # To check whether the form is valid or not
        print(author_form_post.is_valid())
        # To check the form is bound or unbound
        print(author_form_post.is_bound)
        # To display the errors in json
        print(author_form_post.errors.as_json(escape_html=False))
        if (author_form_post.is_valid()):
            author_form_post.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Fail')
# Create your views here.
