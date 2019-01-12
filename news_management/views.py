from django.shortcuts import render, get_object_or_404
from .models import NewsCateory, News
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def get_categories(request):

    news_categories = list(NewsCateory.objects.all().values())
    data =  dict()
    data['news_categories'] = news_categories

    return JsonResponse(data)


#get_news_of_category
# def get_news_of_category(request, category_id):
#     news = News.objects.filter(category = NewsCateory.objects.get(pk=category_name))
#     # print(news)
#     return render(request, "news_management/home.html", {'news':news})

def get_news_of_category(request, category_name):
	news_list = News.objects.filter(category = NewsCateory.objects.get(pk=category_name))
	page = request.GET.get('page',1)

	paginator = Paginator(news_list,3)

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)

	return render(request, "news_management/home.html", {'news':news})


# get news
def get_news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)

    return render(request, "news_management/detail.html", {
        'news':news
    })


#get top news
def get_top_news(request):
    news = list(News.objects.all().values())
    data = dict()
    data['news'] = news

    return JsonResponse(data)


