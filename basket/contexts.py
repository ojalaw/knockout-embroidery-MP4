from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from product.models import Product


def basket_contents(request):
    """ A view that handles basket contents """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    updated_basket = basket.copy()

    for unique_key, item_details in basket.items():
        product_id = item_details.get('product_id')
        quantity = item_details.get('quantity', 0)
        size = item_details.get('size', '')
        colour = item_details.get('colour', '')
        embroidery_location = item_details.get('embroidery_location', '')
        embroidery_text = item_details.get('embroidery_text', '')

        try:
            product = Product.objects.get(pk=product_id)
            subtotal = quantity * product.price
            total += subtotal
            product_count += quantity

            basket_items.append({
                'unique_key': unique_key,
                'quantity': quantity,
                'product': product,
                'size': size,
                'colour': colour,
                'embroidery_location': embroidery_location,
                'embroidery_text': embroidery_text,
                'subtotal': subtotal
            })
        except Product.DoesNotExist:
            del updated_basket[unique_key]
            messages.info(request, f"Removed {unique_key} from your basket as"
                          "it is no longer available.")

    if basket != updated_basket:
        request.session['basket'] = updated_basket

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
