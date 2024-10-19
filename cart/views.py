from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart
from django.contrib import messages

# Create your views here.
def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return resonse
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response

        
def cart_delete(request):
    pass  # Placeholder for cart delete functionality

def cart_update(request):
    cart = Cart(request)

    # Ensure POST request and action is 'post'
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            # Get product ID and quantity from the request
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))

            # Validate product quantity (must be positive)
            if product_qty < 1:
                return JsonResponse({'error': 'Invalid quantity'}, status=400)

            # Update the cart with new quantity
            cart.update(product=product_id, quantity=product_qty)

            # Return the updated quantity as a response
            return JsonResponse({'qty': product_qty, 'product_id':product_id})

        except (ValueError, KeyError):
            return JsonResponse({'error': 'Invalid product or data'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
