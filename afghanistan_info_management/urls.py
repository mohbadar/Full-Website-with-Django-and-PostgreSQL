from django.urls import path, include
from . import views

urlpatterns = [
    path('provinces/', views.get_provinces, name='get_provinces'),
    path(r'province/<province_id>', views.get_province, name='get_province'),
    path(r'district/<district_id>', views.get_district, name='get_district'),
    path(r'area/<area_id>', views.get_area, name='get_area'),


	]
