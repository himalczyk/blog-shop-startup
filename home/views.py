from django.shortcuts import render
from home.models import Product

# Create your views here.
def home_index(request):
    products = Product.objects.all()
    content = {
        'products': products
    }
    return render(request, 'home_index.html', content)

def product_detail(request, pk):
    products = Product.objects.get(pk=pk)
    content = {
        'products': products
    }
    return render(request, 'product_detail.html', content)