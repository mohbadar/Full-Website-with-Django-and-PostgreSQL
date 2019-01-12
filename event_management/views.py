from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Event, EventCategory, EventComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def get_categories(request):

    event_categories = list(EventCategory.objects.all().values())
    data = dict()
    data['event_categories'] = event_categories

    return JsonResponse(data)


# get_top_events
def get_top_events(request):
    events = list(Event.objects.all().values())
    data  = dict()
    data['events'] =events
    return JsonResponse(data)


def get_events_of_category(request, category_id):
	events = Event.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(events,3)

	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)

	return render(request, "event_management/home.html", {'events':events})


# get news
def get_event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, "event_management/detail.html", {
        'event':event
    })
