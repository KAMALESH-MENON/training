from product import Product
from order import Order

class Logic:
    """A class to handle all logic part of order functionality."""
    def __init__(self):
        """Initialize the logic with an empty dict of orders."""
        self.orders = {}

    def place_order(self, order):
        """
        adds order object in orders dictionary.
        
        input: order object
        
        returns: bool
        """
        if order.order_id not in self.orders:
            self.orders[order.order_id] = order
            order.save_to_db()
            return True
        return False

    def list_orders(self):
        """
        return orders list inside a list.
        
        returns: list of orders
        """
        return [str(order) for order in self.orders.values()]

    def calculate_total_cost(self):
        """
        calculate the price of each product in orders
        
        returns: dict with keys calculation_status and total_cost
        """
        total_cost = sum(order.calculate_total() for order in self.orders.values())
        return {"calculation_status": bool(total_cost), "total_cost": total_cost}

    def cancel_order(self, order):
        """
        removes order if order object's id is already in orders dict 
        
        returns: boolean
        """
        if order.order_id in self.orders:
            del self.orders[order.order_id]
            return True
        return False

    def summarize_orders(self):
        """
        returns dict with key total orders, total cost of orders, list of product in the order if any order exist.
        """
        summary = {
            "summary_status": bool(self.orders),
            "total_orders": len(self.orders),
            "total_amount_spent": self.calculate_total_cost()["total_cost"],
            "orders": self.list_orders()
        }
        return summary
