from django.urls import path, include
from . import views

urlpatterns = [
    path('get_categories/', views.get_categories, name="get_article_categories"),
    path('top/', views.get_top_articles, name="get_top_articles"),
    path(r'category/<category_id>/', views.get_articles_of_category, name='articles_of_category'),
    path(r'<article_id>', views.get_article_detail, name="article_detail"),

	]
