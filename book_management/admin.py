from django.contrib import admin
from .models import BookCateory,BookAuthor,Book

# Register your models here.

admin.site.register(BookAuthor)
admin.site.register(BookCateory)
admin.site.register(Book)
