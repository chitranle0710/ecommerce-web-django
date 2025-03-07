from django.shortcuts import render, get_object_or_404
from store.models import Product, Profile
from django.http import JsonResponse
from .cart import Cart
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities,"totals": totals})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Sản phẩm đã được thêm vào giỏ hàng..."))
        return response

        
def cart_delete(request):
    cart = Cart(request)
    product_id = str(request.POST.get('product_id'))  # Ensure product ID comes from the request

    if product_id in cart.cart:
        del cart.cart[product_id]

    cart.session.modified = True

    if request.user.is_authenticated:
        current_user = Profile.objects.filter(user__id=request.user.id)
        
        carty = str(cart.cart).replace("'", '"')

        current_user.update(old_cart=str(carty))
    
    return JsonResponse({'message': 'Sản phẩm đã được xóa khỏi giỏ hàng'})

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("Giỏ hàng đã được cập nhật"))
        return response
