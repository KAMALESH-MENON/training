class Product:
    """A class to handle product functionality."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"[product id: {self.product_id}, name: {self.name}, price:{self.price}]"
