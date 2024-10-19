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

    def add(self, product):
        product_id = str(product.id)  # Use string for consistency

        if product_id in self.cart:
            # Increment the quantity if already in the cart
            self.cart[product_id]['quantity'] += 1
        else:
            # Add new product with initial quantity
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': 1,  # Set initial quantity to 1
                'name': product.name,
                'sale_price': str(product.sale_price) if product.is_sale else None
            }

        # Mark the session as modified to ensure changes are saved
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
