from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from .models import Product, Review

def review(request):
    reviews = Review.objects.all()
    return render(request, 'product/reviews.html', {'reviews': reviews})

def products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'product/product.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    
      
    if not str(product_id).isnumeric():
     raise Http404('Invalid product id')

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)