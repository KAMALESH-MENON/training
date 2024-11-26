"""product class"""
class Product:
    """product class"""
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"product id: {self.id}, name: {self.name}, price: {self.price}"
