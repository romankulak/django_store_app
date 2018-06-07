import logging
from functools import wraps

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book
from .models import WebRequest


logger = logging.getLogger(__name__)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'{func.__name__} Was called')
        return func(*args, **kwargs)
    return wrapper


def book_list(request, status=None):
    if status == 'published':
        object_list_query = Book.published
    elif status == 'draft':
        object_list_query = Book.draft
    else:
        object_list_query = Book.objects

    object_list = object_list_query.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        books = paginator.page(1)

    return render(
        request,
        'book_store/books/list.html',
        {
            'page': page,
            'books': books,
        },
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(
        request,
        'book_store/books/detail.html',
        {
            'book': book,
        },
    )


@log
@login_required
def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.publisher = request.user
            book.save()
            return redirect(
                'book_store.views.book_detail',
                pk=book.pk
            )
    else:
        form = BookForm()
    return render(request, 'book_store/books/edit.html', {'form': form})


@log
@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.publisher = request.user
            book.save()
            return redirect('book_store:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_store/books/edit.html', {'form': form})


@log
@login_required
def book_remove(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_store:book_list')


@login_required
def book_change_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.is_published():
        book.change_status('draft')
    else:
        book.change_status('published')
    return redirect('book_store:book_detail', pk=pk)


@login_required
def view_requests(request, count=10):
    web_requests = WebRequest.objects.order_by('-id')[:count]
    return render(
        request,
        'book_store/web_requests/list.html',
        {
            'web_requests': web_requests
        }
    )


