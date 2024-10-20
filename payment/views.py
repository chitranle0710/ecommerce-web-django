from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product, Profile
import datetime

# Import Some Paypal Stuff
from django.urls import reverse
from django.conf import settings
import uuid # unique user id for duplictate orders

def process_order(request):
    if request.POST:
        # Get the cart
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Get Shipping Session Data
        my_shipping = request.session.get('my_shipping')

        # Check if shipping information is available
        if my_shipping is None:
            messages.error(request, "Shipping information is missing. Please fill out the shipping form.")
            return redirect('checkout')  # Redirect to the checkout or shipping page

        # Gather Order Info
        full_name = my_shipping.get('shipping_full_name', '')  # Use get to avoid KeyError
        email = my_shipping.get('shipping_email', '')
        
        # Create Shipping Address from session info
        shipping_address = f"{my_shipping.get('shipping_address1', '')}\n{my_shipping.get('shipping_address2', '')}\n{my_shipping.get('shipping_city', '')}\n{my_shipping.get('shipping_state', '')}\n{my_shipping.get('shipping_zipcode', '')}\n{my_shipping.get('shipping_country', '')}"
        amount_paid = totals

        # Create an Order
        if request.user.is_authenticated:
            # logged in
            user = request.user
            # Create Order
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            # Get the order ID
            order_id = create_order.pk

            # Add order items
            for product in cart_products():
                # Get product ID
                product_id = product.id
                # Get product price
                price = product.sale_price if product.is_sale else product.price

                print(f"Price for product {product_id}: {price}")

                # Get quantity
                for key, value in quantities().items():
                    if int(key) == product.id:
                        # Create order item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
                        create_order_item.save()

            # Clear the cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]

            # Delete Cart from Database (old_cart field)
            Profile.objects.filter(user__id=request.user.id).update(old_cart="")

            messages.success(request, "Đơn hàng đã được đặt!!")
            return redirect('home')

        else:
            # not logged in
            # Create Order
            create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            # Get the order ID
            order_id = create_order.pk

            # Add order items
            for product in cart_products():
                product_id = product.id
                price = product.sale_price if product.is_sale else product.price

                for key, value in quantities().items():
                    if int(key) == product.id:
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                        create_order_item.save()

            # Clear the cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]

            messages.success(request, "Order Placed!")
            return redirect('home')

    else:
        messages.success(request, "Access Denied")
        return redirect('home')



def billing_info(request):
    if request.POST:
        # Get the cart
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Store shipping information in the session
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        if request.user.is_authenticated:
            # Get The Billing Form
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_info": request.POST,
                "billing_form": billing_form
            })

        else:
            # Not logged in
            # Get The Billing Form
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_info": request.POST,
                "billing_form": billing_form
            })

    else:
        messages.success(request, "Truy cập bị từ chối")
        return redirect('home')



def checkout(request):
	# Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # Checkout as logged in user
        # Shipping User
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        # Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})

def payment_success(request):
	return render(request, 'payment/payment_success.html',{})
