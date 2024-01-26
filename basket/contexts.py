from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Product


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for unique_key, item_details in basket.items():
        product_id = item_details.get('product_id')
        quantity = item_details.get('quantity', 0)
        size = item_details.get('size', '')
        colour = item_details.get('colour', '')
        embroidery_location = item_details.get('embroidery_location', '')
        embroidery_text = item_details.get('embroidery_text', '')

        if product_id and quantity:
            product = get_object_or_404(Product, pk=product_id)
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