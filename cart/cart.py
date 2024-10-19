from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        # Store the request for future use
        self.request = request
        
        # Try to retrieve the 'cart' from the session, or initialize it as an empty dictionary if it doesn't exist
        cart = self.session.get('cart')
        
        if not cart:
            # If the cart does not exist, create an empty cart and store it in the session
            cart = self.session['cart'] = {}
        
        # Make the cart accessible throughout the Cart class
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return sum(item for item in self.cart.values())


    def get_prods(self):
    	product_ids = self.cart.keys()
    	products = Product.objects.filter(id__in=product_ids)

    	return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # Get cart
        ourcart = self.cart
        # Update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True
    

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save carty to the Profile Model
            current_user.update(old_cart=str(carty))


        thing = self.cart
        return thing






