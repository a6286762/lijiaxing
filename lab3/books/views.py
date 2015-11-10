# Create your views here.
# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from books.models import Book, Author
# meiyongdedongsisan
# duojiadesan
def search_form(request):
    return render_to_response('Search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(authorid__Name__icontains=q)
            return render_to_response('Search_result.html',
                    {'books': books, 'query': q})
    return render_to_response('Search_form.html',
            {'errors': errors })
            
def look(request):
    if 'q' in request.GET:
        q = request.GET['q']
        book = Book.objects.get(ISBN=q)
    return render_to_response('look_result.html',{'book':book,'Authors':book.authorid.all() })
def delete(request):   
    if 'q' in request.GET:
        q = request.GET['q']
        book = Book.objects.get(Title=q)
        book.delete()
    return render_to_response('deleteok.html')
