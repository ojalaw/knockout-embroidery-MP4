from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all() 
    context = {
        'products': products,
    }
    return render(request, 'home/home.html', context)

def about_us(request):
    return render(request, 'home/about_us.html')