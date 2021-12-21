from django.shortcuts import render
from home.models import Post

# Create your views here.
def home_index(request):
    posts = Post.objects.all()
    content = {
        'posts': posts
    }
    return render(request, 'home_index.html', content)

def post_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    content = {
        'posts': posts
    }
    return render(request, 'post_detail.html', content)