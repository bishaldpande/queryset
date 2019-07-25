from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_page
# Create your views here.

from .models import Book, Author

def book_detail1(request):
    book = Book.objects.all()
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/book.html', {'books': books})


def book_detail2(request):
    book = Book.objects.all().select_related('publisher', 'genre').prefetch_related('author')
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/book.html', {'books': books})


@cache_page(60 * 15)
def book_detail3(request):
    book = Book.objects.all()
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/book.html', {'books': books})


def ids1(request):
    book = Book.objects.all()
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/ids1.html', {'books': books})


def ids2(request):
    book = Book.objects.all()
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/ids2.html', {'books': books})


def ids3(request):
    book = Book.objects.all().prefetch_related('author')
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/ids2.html', {'books': books})


def ids4(request):
    book = Book.objects.all().prefetch_related("author")
    paginator = Paginator(book, 1000)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book/ids3.html', {'books': books})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('all_books_2')
    
    return redirect(login)