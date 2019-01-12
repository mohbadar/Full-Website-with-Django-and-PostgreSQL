from django.shortcuts import render,get_object_or_404
from .models import ArticleCateory, Article
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


# get_categories
def get_categories(request):
    article_categories = list(ArticleCateory.objects.all().values())

    data = dict()
    data['article_categories'] = article_categories

    return JsonResponse(data)

def get_top_articles(request):
    articles = list(Article.objects.all().values())
    data = dict()
    data['articles']= articles
    return JsonResponse(data)


def get_articles_of_category(request, category_id):
	articles = Article.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(articles,3)

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)

	return render(request, "article_management/home.html", {'articles':articles})


# get news
def get_article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, "article_management/detail.html", {
        'article':article
    })
