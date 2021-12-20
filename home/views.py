from django.shortcuts import render
from home.models import Post

# Create your views here.
def home_index(request):
    post = Post.objects.all()
    content = {
        'post': post
    }
    return render(request, 'home_index.html', content)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    content = {
        'post': post
    }
    return render(request, 'post_detail.html', content)