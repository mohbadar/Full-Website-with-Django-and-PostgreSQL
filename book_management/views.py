from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import BookCateory, Book, BookAuthor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def get_categories(request):

    book_categories = list(BookCateory.objects.all().values())
    data = dict()

    data['book_categories'] = book_categories

    return JsonResponse(data)


def get_top_books(request):
    books = list(Book.objects.all().values())
    data = dict()
    data['books'] = books
    return JsonResponse(data)

def get_books_of_category(request, category_id):
	books = Book.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(books,3)

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)

	return render(request, "book_management/home.html", {'books':books})


# get news
def get_book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(request, "book_management/detail.html", {
        'book':book
    })

def get_author(request, author_id):

    author = get_object_or_404(BookAuthor, id= author_id)
    return render(request, "book_management/author.html", {'author':author})
