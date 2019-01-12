from django.shortcuts import render, get_object_or_404
from .models import Page , PageCategory
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def get_categories(request):
    page_categories = list(PageCategory.objects.all().values())
    data = dict()
    data['page_categories'] = page_categories
    return JsonResponse(data)

def get_top_pages(request):
    pages = list(Page.objects.all().values())
    data = dict()
    data['pages'] = pages
    return JsonResponse(data)


def get_pages_of_category(request, category_id):
	pages = Page.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(pages,3)

	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except EmptyPage:
		pages = paginator.page(paginator.num_pages)

	return render(request, "mesc_management/home.html", {'pages':pages})


# get news
def get_page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    return render(request, "mesc_management/detail.html", {
        'page':page
    })
