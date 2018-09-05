from django.shortcuts import get_object_or_404
from products.models import Lamp


def get_cart_items_and_total(cart):
    total = 0
    cart_items = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Lamp, pk=lamp_id)
        item_total = quantity * product.bruto_price
        total += item_total
        cart_items.append({'product':product, 'quantity': quantity, 'total': item_total}) 
        
        
    return {'cart_items' : cart_items, 'total': total}