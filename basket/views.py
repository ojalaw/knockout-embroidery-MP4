from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from product.models import Product

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    basket = request.session.get('basket', {})

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size', product.size)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in basket:
        if size in basket[item_id]['items_by_size']:
            basket[item_id]['items_by_size'][size] += quantity  
        else:
            basket[item_id]['items_by_size'][size] = quantity   
    else:
        basket[item_id] = {
            'items_by_size': {
                size: quantity
            }
        }

    messages.success(request, 'Added to basket')
        
    request.session['basket'] = basket
    return redirect(redirect_url)

def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')
    basket = request.session.get('basket', {})

    if item_id in basket:
        if size in basket[item_id]['items_by_size']:
            if quantity >= 1:
                basket[item_id]['items_by_size'][size] = quantity
            else:
                del basket[item_id]['items_by_size'][size]
                if not basket[item_id]['items_by_size']:
                    del basket[item_id]
        elif size:
            if quantity >= 1:
                basket[item_id]['items_by_size'][size] = quantity
            else:
                del basket[item_id]
        else:
            messages.error(request, "Size information missing for the item.")
    else:
        messages.error(request, "Item not found in basket.")

    request.session['basket'] = basket
    messages.success(request, 'Basket updated successfully.')

    return redirect(reverse('view_basket'))

def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)