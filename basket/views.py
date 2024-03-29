from django.shortcuts import render, reverse, redirect, get_object_or_404
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

    unique_key = (
    f"{item_id}_{size}_{colour}_{embroidery_location}"
    f"_{embroidery_text}"
)

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


def remove_from_basket(request, unique_key):
    """Remove the item basket identified by the unique key."""

    basket = request.session.get('basket', {})

    if unique_key in basket:
        del basket[unique_key]

    request.session['basket'] = basket
    messages.success(request, 'Item removed from your basket.')
    return redirect('view_basket')
