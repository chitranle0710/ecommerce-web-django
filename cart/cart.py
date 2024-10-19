from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key!  Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)  # Convert product ID to string to use as key

        if product_id in self.cart:
            # If product is already in the cart, increment the quantity
            self.cart[product_id]['quantity'] += quantity
        else:
            # If product is not in the cart, add it with the specified quantity
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': quantity,
                'name': product.name,
                'sale_price': str(product.sale_price) if product.is_sale else None
            }

        # Mark the session as modified to ensure the cart is saved
        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_prods(self):
    	product_ids = self.cart.keys()
    	products = Product.objects.filter(id__in=product_ids)

    	return products

    def get_quants(self):
        quantities = self.cart
        return quantities






