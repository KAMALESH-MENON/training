from db import get_db_connection
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
        
        input: product object
        
        returns: bool
        """
        if isinstance(new_product, Product):
            self.products.append(new_product)
            self.total += new_product.price
            return True
        return False

    def calculate_total(self):
        """
        calculates total price of each product in products list
        
        returns: float (total price of all products)
        """
        return sum(product.price for product in self.products)

    def save_to_db(self):
        conn = get_db_connection()
        product_ids = ','.join([str(product.product_id) for product in self.products])
        with conn:
            conn.execute('INSERT OR REPLACE INTO orders (order_id, product_ids, total) VALUES (?, ?, ?)',
                         (self.order_id, product_ids, self.calculate_total()))

    @staticmethod
    def load_from_db(order_id):
        conn = get_db_connection()
        order_data = conn.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,)).fetchone()
        if order_data:
            order = Order(order_data[0])
            product_ids = order_data[1].split(',')
            for product_id in product_ids:
                product = Product.load_from_db(int(product_id))
                if product:
                    order.add_product(product)
            return order
        return None

    def __str__(self):
        products_str = ', '.join(str(product) for product in self.products)
        return f"Order ID: {self.order_id}, Products: [{products_str}], Total: {self.calculate_total()}"
