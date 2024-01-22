from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from product.models import Product

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """

    request.session['show_basket_in_toast'] = False
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    basket = request.session.get('basket', {})

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size', product.size)
    colour = request.POST.get('product_colour', product.colour)
    embroidery_location = request.POST.get('embroidery_location', '')
    embroidery_text = request.POST.get('embroidery_text', '')
    redirect_url = request.POST.get('redirect_url')

    # Create a unique key for each item variant
    unique_key = f"{item_id}_{size}_{colour}_{embroidery_location}_{embroidery_text}"

    if unique_key in basket:
        basket[unique_key]['quantity'] += quantity
    else:
        basket[unique_key] = {
            'quantity': quantity,
            'product_id': item_id,
            'size': size,
            'colour': colour,
            'embroidery_location': embroidery_location,
            'embroidery_text': embroidery_text
        }

    messages.success(request, f'Added {product.name} to your basket.')

    request.session['basket'] = basket
    request.session['show_basket_in_toast'] = True
    return redirect(redirect_url)

def adjust_basket(request, unique_key):
    """Adjust the quantity of the specified product variant in the basket."""

    basket = request.session.get('basket', {})
    quantity = int(request.POST.get('quantity'))

    if unique_key in basket:
        if quantity > 0:
            basket[unique_key]['quantity'] = quantity
        else:
            del basket[unique_key]

    request.session['basket'] = basket
    messages.success(request, 'Basket updated successfully.')
    return redirect('view_basket')

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