# Importing necessary modules
from product import Product

class Order:
    """A class to handle order functionality."""

    def __init__(self, order_id):
        """Initialize the Order with order_id"""
        self.order_id = order_id
        self.products = []
        self.total = 0

    def add_product(self, new_product):
        """
        adds new_product object in products list
        
        input : product object
        
        returns : bool
        """
        if isinstance(new_product, Product):
            self.products.append(new_product)
            self.total += new_product.price
            return True
        return False

    def calculate_total(self):
        """
        calculates total price of each product in products list
        
        returns : float (total price of all products)
        """
        return sum(product.price for product in self.products)

    def __str__(self):
        products_str = ', '.join(str(product) for product in self.products)
        return f"Order ID: {self.order_id}, Products: [{products_str}], Total: {self.calculate_total()}"
