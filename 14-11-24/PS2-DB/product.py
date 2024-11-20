from db import get_db_connection

class Product:
    """A class to handle product functionality."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"[product id: {self.product_id}, name: {self.name}, price: {self.price}]"

    def save_to_db(self):
        conn = get_db_connection()
        with conn:
            conn.execute('INSERT OR REPLACE INTO products (product_id, name, price) VALUES (?, ?, ?)',
                         (self.product_id, self.name, self.price))

    @staticmethod
    def load_from_db(product_id):
        conn = get_db_connection()
        product_data = conn.execute('SELECT * FROM products WHERE product_id = ?', (product_id,)).fetchone()
        if product_data:
            return Product(product_data[0], product_data[1], product_data[2])
        return None
