from product import Product
from order import Order
import csv

class Logic:
    """A class to handle all logic part of order functionality."""
    def __init__(self):
        """Initialize the login with an empty dict of orders."""
        self.orders = {}

    def place_order(self, order):
        """
        adds order object in orders dictionary.
        
        input : order object
        
        returns : bool
        """
        if order.order_id not in self.orders:
            self.orders[order.order_id] = order
            return True
        return False

    def list_orders(self):
        """
        return orders list inside a list.
        
        input : order object
        
        returns : lsit of 
        """
        return [str(order) for order in self.orders.values()]

    def calculate_total_cost(self):
        """
        calculate the price of each product in orders
        
        return: dict with keys calculation_status and total_cost
        
        """
        temp = {"calculation_status" : False, "total_cost" : 0}
        cost = sum(order.calculate_total() for order in self.orders.values())

        if cost!=0:
            temp["calculation_status"] = True
            temp["total_cost"] = cost
        return temp

    def cancel_order(self, order):
        """
        removes order if order object's id in already in orders dict 
        
        return: boolean
        """
        if order.order_id in self.orders:
            del self.orders[order.order_id]
            return True
        return False

    def summarize_orders(self):
        """
        returns dict with key total orders total, cost of order, list of product in the order if any order exist.
        """
        temp = {"summary_status": False, "total_orders": 0, "total_amount_spent": 0,  "orders": []}

        total_order = len(self.orders)
        if total_order!=0:
            temp["summary_status"] = True
            temp["total_orders"] =  total_order
            temp["total_amount_spent"] = self.calculate_total_cost()["total_cost"]
            temp["orders"] = self.list_orders()

        return temp
