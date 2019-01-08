from django.contrib import admin
from .models import Article, ArticleCateory, ArticleSource, ArticleAuthor

# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleCateory)
admin.site.register(ArticleAuthor)
admin.site.register(ArticleSource)
admin.site.site_header = "Afghan Portal System"