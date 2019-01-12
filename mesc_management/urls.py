from django.urls import path, include
from . import views

urlpatterns = [
    path('get_categories/', views.get_categories, name='get_page_categories'),
    path('top/', views.get_top_pages, name='get_top_pages'),
    path(r'page/category/<category_id>/', views.get_pages_of_category, name='pages_of_category'),
    path(r'page/<page_id>', views.get_page_detail, name="page_detail"),
	]
