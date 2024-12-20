from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    return render(
        request,
        'books/books_list.html',
        context={
            'books': Book.objects.all(),
        }
    )


def book(request, pub_date):
    return render(
        request,
        'books/book.html',
        context={
            'book': get_object_or_404(Book, pub_date=pub_date),
            'next_page': Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first(),
            'previous_page': Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first(),
        }
    )
