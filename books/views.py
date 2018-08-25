from django.shortcuts import render
from  django.http import HttpResponse
from books.models import Book


def search_form(request):
    return render(request, 'search_form.html')
def search_form2(request):
    return render(request, 'search_form2.html')

def search_form3(request):
    return render(request, 'search_form3.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def search2(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',{'books': books, 'query': q})
    else:
        # return HttpResponse('Please submit a search term.')
        return render (request, 'search_form2.html', {'error': True})

def search2(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',{'books': books, 'query': q})
    else:
        # return HttpResponse('Please submit a search term.')
        return render (request, 'search_form2.html', {'error': True})

def search3(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',{'books': books, 'query': q})
    return render(request, 'search_form2.html',{'error': error})

def search4(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',{'books': books, 'query': q})
    return render(request, 'search_form4.html',{'errors': errors})



