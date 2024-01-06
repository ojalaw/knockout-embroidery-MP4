from django.shortcuts import render, redirect, get_object_or_404
from .models import BasketItem
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def basket_detail(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    return render(request, 'basket/basket.html', {'basket_items': basket_items})

@login_required
@require_POST
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
    basket_item, created = BasketItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        basket_item.quantity += quantity
    else:
        basket_item.quantity = quantity
    basket_item.save()
    return JsonResponse({'success': True, 'message': 'Product added to basket'})

@login_required
def remove_from_basket(request, basket_item_id):
    basket_item = get_object_or_404(BasketItem, id=basket_item_id, user=request.user)
    basket_item.delete()
    return redirect('basket_detail')