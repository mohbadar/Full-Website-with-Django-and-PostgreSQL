from django.urls import path
from . import views


urlpatterns = [
    path('get_categories/', views.get_categories, name="get_book_categories"),
    path('top/', views.get_top_books, name='get_top_books'),
    path(r'category/<category_id>/', views.get_books_of_category, name='book_of_category'),
    path(r'<book_id>', views.get_book_detail, name="book_detail"),
    path(r'author/<author_id>', views.get_author, name="get_author")

	]

