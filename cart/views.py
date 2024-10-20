from django.shortcuts import render, get_object_or_404
from store.models import Product, Profile
from django.http import JsonResponse
from .cart import Cart
from django.contrib import messages

# Create your views here.
def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities,"totals": totals})

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
        messages.success(request, ("Sản phẩm đã được thêm vào giỏ hàng..."))
        return response

        
def cart_delete(request):
    cart = Cart(request)
    product_id = str(request.POST.get('product_id'))  # Ensure product ID comes from the request

    # Delete from dictionary/cart
    if product_id in cart.cart:
        del cart.cart[product_id]

    cart.session.modified = True

    # Deal with logged-in user
    if request.user.is_authenticated:
        # Get the current user profile
        current_user = Profile.objects.filter(user__id=request.user.id)
        
        # Convert {'3': 1, '2': 4} to {"3": 1, "2": 4}
        carty = str(cart.cart).replace("'", '"')

        # Save carty to the Profile Model
        current_user.update(old_cart=str(carty))
    
    return JsonResponse({'message': 'Sản phẩm đã được xóa khỏi giỏ hàng'})

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        #return redirect('cart_summary')
        messages.success(request, ("Giỏ hàng đã được cập nhật"))
        return response
