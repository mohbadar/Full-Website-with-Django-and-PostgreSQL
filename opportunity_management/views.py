from django.shortcuts import render, get_object_or_404
from .models import OpportunityCategory, Opportunity
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def get_categories(request):

    categories = list(OpportunityCategory.objects.all().values())
    data = dict()
    data['opportunity_categories'] = categories
    return JsonResponse(data)


def get_opportunities_of_category(request, category_id):
	opportunities = Opportunity.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(opportunities,3)

	try:
		opportunities = paginator.page(page)
	except PageNotAnInteger:
		opportunities = paginator.page(1)
	except EmptyPage:
		opportunities = paginator.page(paginator.num_pages)

	return render(request, "opportunity_management/home.html", {'opportunities':opportunities})


# get news
def get_opportunity_detail(request, opportunity_id):
    opportunity = get_object_or_404(Opportunity, id=opportunity_id)

    return render(request, "opportunity_management/detail.html", {
        'opportunity':opportunity
    })
