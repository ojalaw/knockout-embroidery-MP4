from django.shortcuts import render, redirect  
from django.http import HttpResponse
from .models import BasketItem  
from product.models import Product

def basket_detail(request):

    items = BasketItem.objects.filter(user=request.user)
    context = {'items': items}
    return render(request, 'basket/basket.html', context)


def add_to_basket(request):
    
    product_id = request.POST['product_id']
    quantity = request.POST['quantity']
    
    product = Product.objects.get(pk=product_id)
    
    item, created = BasketItem.objects.get_or_create(
        product=product, 
        user=request.user, 
        defaults={'quantity': quantity}
    )

    if not created:
        item.quantity += quantity
        item.save() 
        
    return redirect('product_detail', product.id)

def remove_from_basket(request, item_id):
   
    item = BasketItem.objects.get(pk=item_id)
    item.delete()
    
    return HttpResponse(status=200)
    
def basket_summary(request):
    
    items = BasketItem.objects.filter(user=request.user)
    total = sum(item.quantity * item.product.price for item in items)
    
    context = {
       'items': items,
       'total': total
    }
    
    return render(request, 'basket/basket.html', context)