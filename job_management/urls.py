from django.urls import path, include
from . import views

urlpatterns = [
    path('get_categories/', views.get_categories, name='get_job_categories'),
    path(r'category/<category_id>/', views.get_jobs_of_category, name='jobs_of_category'),
    path(r'entity/<entity_id>', views.get_entity, name='get_entity'),
    path(r'<job_id>', views.get_job_detail, name="job_detail"),

	]
