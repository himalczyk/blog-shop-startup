from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# Create your views here.

class NewsPageView(ListView):
    template_name = "news.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter().order_by("-pub_date")[:10]
        return context