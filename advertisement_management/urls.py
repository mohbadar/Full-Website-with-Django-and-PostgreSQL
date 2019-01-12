from django.urls import path, include
from . import views


urlpatterns = [
    path('get_categories/', views.get_categories, name="get_advertisement_categories"),

]
