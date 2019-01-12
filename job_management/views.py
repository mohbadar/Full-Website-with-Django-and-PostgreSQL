from django.shortcuts import render, get_object_or_404
from .models import Job , JobCategory, Entity
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_categories(request):
    job_categories = list(JobCategory.objects.all().values())
    data = dict()
    data['job_categories'] = job_categories
    return JsonResponse(data)

def get_jobs_of_category(request, category_id):
	jobs = Job.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(jobs,3)

	try:
		jobs = paginator.page(page)
	except PageNotAnInteger:
		jobs = paginator.page(1)
	except EmptyPage:
		jobs = paginator.page(paginator.num_pages)

	return render(request, "job_management/home.html", {'jobs':jobs})


# get news
def get_job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(request, "job_management/detail.html", {
        'job':job
    })

def get_entity(request, entity_id):
    entity = get_object_or_404(Entity, id=entity_id)
    return render(request, 'job_management/entity.html', {'entity': entity})
