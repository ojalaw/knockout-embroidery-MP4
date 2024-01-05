from django.shortcuts import render
from .models import Product, Review

def product(request):
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})

def review(request):
    reviews = Review.objects.all()
    return render(request, 'product/reviews.html', {'reviews': reviews})