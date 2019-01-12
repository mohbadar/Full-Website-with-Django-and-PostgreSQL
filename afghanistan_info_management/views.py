from django.shortcuts import render, get_object_or_404
from .models import Province, Destrict , Area
from django.http import JsonResponse

# Create your views here.

def get_provinces(request):

    provinces = list(Province.objects.all().values())
    data = dict()

    data['provinces'] = provinces
    return JsonResponse(data)


def get_province(request, province_id):

    province = get_object_or_404(Province, id=province_id)
    return render(request, 'afghanistan_info_management/province.html', {'province':province})

def get_district(request, district_id):

    district = get_object_or_404(Destrict, id=district_id)
    return render(request, 'afghanistan_info_management/district.html', {'district':district})


def get_area(request, area_id):

    area = get_object_or_404(Area, id=area_id)
    return render(request, 'afghanistan_info_management/area.html', {'area':area})
