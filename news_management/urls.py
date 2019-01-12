from django.urls import path, include
from . import views

urlpatterns = [
    path('get_categories/', views.get_categories, name="get_news_categories"),
    path('category/<str:category_name>', views.get_news_of_category, name="get_news_of_category"),
    path('top/', views.get_top_news, name="get_top_news"),
    path('<str:slug>/', views.get_news_detail, name="get_news_detail"),


	]
