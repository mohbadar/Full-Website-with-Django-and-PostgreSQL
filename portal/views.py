from django.shortcuts import render
from article_management import models

# Create your views here.

def index(request):
    articles  = models.Article.objects.first()
    return render(request, "index.html",{'articles':articles})
