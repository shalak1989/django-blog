from django.shortcuts import render
from django.utils import timezone
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    data = {'posts': posts}
    return render(request, 'blog/post_list.html', data)

