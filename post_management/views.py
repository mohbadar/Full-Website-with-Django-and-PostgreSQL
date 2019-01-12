from django.shortcuts import render, get_object_or_404
from .models import Post, PostCategory, PostComment
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def get_categories(request):

    post_categories = list(PostCategory.objects.all().values())
    data = dict()
    data['post_categories'] = post_categories

    return JsonResponse(data)


def get_posts_of_category(request, category_id):
	posts = Post.objects.filter(category = category_id)
	page = request.GET.get('page',1)

	paginator = Paginator(posts,3)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, "post_management/home.html", {'posts':posts})


# get news
def get_post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, "post_management/detail.html", {
        'post':post
    })
