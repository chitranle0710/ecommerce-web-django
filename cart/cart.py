from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request

        # Get the current cart from the session, or create a new one if it doesn't exist
        cart = self.session.get('session_key')

        if cart is None:
            # Initialize the cart if it doesn't exist
            cart = self.session['session_key'] = {}

        # Ensure that self.cart is assigned to the existing or new cart
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






