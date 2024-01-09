from django.shortcuts import get_object_or_404, render  
from django.http import HttpResponse
from .models import BasketItem  
from product.models import Product

def add_to_basket(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    
    BasketItem.objects.create(
        user=request.user, 
        product=product
    )

    return HttpResponse() 
    
        
def basket_detail(request):
   
    items = BasketItem.objects.filter(user=request.user)
    context = {
        'items': items
    }

    return render(request, 'basket/basket.html', context)