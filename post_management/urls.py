from django.urls import path
from . import views


urlpatterns = [
    path('get_categories/', views.get_categories, name="get_post_categories"),
    path(r'category/<category_id>/', views.get_posts_of_category, name='posts_of_category'),
    path(r'<post_id>', views.get_post_detail, name="post_detail"),

	]

