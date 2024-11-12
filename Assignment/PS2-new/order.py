"""order class"""
from product import products
class Order:
    """order class"""
    def __init__(self, order_id):
        self.order_id = order_id
        self.orders = []
        self.total = 0

    def __str__(self):
        return f"order id : {self.order_id}, products: {self.orders}, total: {self.calculate_total(self.order_id)}"

    def add_product_in_orders(self, product):
        if product in products:
            self.orders.append(product)
            return True
    
    def total_cost(self, orders):
        return sum(product.price for product in self.orders) 
    
    
    def add_product(self, order_id, product):
        """add product to orderdict """
        self.order_dict[order_id].append(product)
        return self.order_dict

    def calculate_total(self, order_id):
        """adds product to the products_li"""
        total = 0
        for product in self.order_dict[order_id]:
            total += product.price
        return total

    def delete_order(self, order_id):
        if order_id in self.order_dict.keys():
            del self.order_dict[order_id]
            return True
        return False
    