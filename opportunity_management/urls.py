from django.urls import path, include
from . import views

urlpatterns = [
    path('get_categories/', views.get_categories, name='get_opportunity_category'),
    path(r'category/<category_id>/', views.get_opportunities_of_category, name='opportunities_of_category'),
    path(r'<opportunity_id>', views.get_opportunity_detail, name="get_opportunity_detail"),

	]
