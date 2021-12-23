from django.shortcuts import render
from about.models import About

# Create your views here.
def about_us(request):
    abouts = About.objects.all()
    content = {
        'abouts': abouts
    }
    return render(request, 'about_index.html', content)