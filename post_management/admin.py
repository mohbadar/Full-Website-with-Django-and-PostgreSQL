from django.contrib import admin
from .models import Post, PostCategory, PostComment

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostComment)
