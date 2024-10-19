from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart

# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)

        response = JsonResponse({'Product Name': product.name})  # Fixed key name syntax
        return response
        
def cart_delete(request):
    pass  # Placeholder for cart delete functionality

def cart_update(request):
    pass  # Placeholder for cart update functionality
