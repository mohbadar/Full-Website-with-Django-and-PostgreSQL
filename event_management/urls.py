from django.urls import path, include
from . import views

urlpatterns = [
    path('get_categories/', views.get_categories, name="get_event_categories"),
    path('top', views.get_top_events , name='get_top_events'),
    path(r'category/<category_id>/', views.get_events_of_category, name='event_of_category'),
    path(r'<event_id>', views.get_event_detail, name="event_detail"),

	]
