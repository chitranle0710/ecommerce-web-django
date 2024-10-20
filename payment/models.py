from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShippingAddress(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
	fshipping_ull_name = models.CharField(max_length = 255)
	shipping_email = models.CharField(max_length = 255)
	shipping_address1 = models.CharField(max_length = 255)
	shipping_address2 = models.CharField(max_length = 255)
	shipping_city = models.CharField(max_length = 255)
	shipping_state = models.CharField(max_length = 255, null = True, blank = True)
	shipping_zipcode = models.CharField(max_length = 255, null = True, blank = True)
	shipping_ountry = models.CharField(max_length = 255)

	class Meta:
		verbose_name_plural = "ShippingAddress"

	def __str__(self):
		return f'Shipping address - {str(self.id)}'