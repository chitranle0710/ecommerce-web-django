from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

# Register your models here on the section admin.
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)


