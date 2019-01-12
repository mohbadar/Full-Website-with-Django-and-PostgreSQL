from django.shortcuts import render
from .models import AdvertisementCategory, Advertisement
from django.http import JsonResponse


# Create your views here.

def get_categories(request):

    advertisement_categories = list(AdvertisementCategory.objects.all().values())
    data = dict()
    data['advertisement_categories'] = advertisement_categories
    return JsonResponse(data)
