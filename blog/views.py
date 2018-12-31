from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    data = {'posts': posts}
    return render(request, 'blog/post_list.html', data)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {'post': post}
    return render(request, 'blog/post_detail.html', data)

