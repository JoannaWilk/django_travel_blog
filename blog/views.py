from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# Create your views here.
def post_list(request):
    object_list = Post.published.all()
    # let's set 3 posts per page
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish_date__year=year,
                             publish_date__month=month,
                             publish_date__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def about(request):
    return render(request, 'blog/sitepage/about.html')
