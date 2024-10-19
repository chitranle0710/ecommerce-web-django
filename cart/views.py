from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods

    return render(request, 'cart_summary.html', {"cart_products": cart_products})

def cart_add(request):
       # Get the cart
    cart = Cart(request)

    # Test for POST
    if request.POST.get('action') == 'post':
        # Get product ID and quantity from the request
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Look up product in the database
        product = get_object_or_404(Product, id=product_id)

        # Add product to the cart with the specified quantity
        cart.add(product=product, quantity=product_qty)

        # Get updated cart quantity (total number of items)
        cart_quantity = cart.__len__()

        # Return response with updated cart quantity
        response = JsonResponse({'qty': cart_quantity})
        return response
        
def cart_delete(request):
    pass  # Placeholder for cart delete functionality

def cart_update(request):
    pass  # Placeholder for cart update functionality
