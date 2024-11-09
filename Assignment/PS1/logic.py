"""logic part of PS1"""
class Logic:
    """logic part of PS1"""
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """add product to products"""
        if product in self.products:
            return False
        self.products.append(product)
        return True

    def list_products(self):
        """list all products"""
        if self.products:
            return self.products
        return False

    def update_product(self, product_id, price):
        """update the price of given product_id"""
        for product in self.products:
            if product.id == product_id:
                product.price = price
                return True
        return False

    def apply_discount(self, discount_percentage):
        """apply discount to all products"""
        if self.products:
            for product in self.products:
                product.price = product.price - (product.price * (discount_percentage/100))
            return True
        return False
