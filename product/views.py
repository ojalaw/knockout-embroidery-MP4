from django.shortcuts import render, get_object_or_404
from .models import Product, Review

def review(request):
    reviews = Review.objects.all()
    return render(request, 'product/reviews.html', {'reviews': reviews})

def products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product/product.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)