from product import Product
import csv
import os
"""logic part of PS1"""
class Logic:
    """logic part of PS1"""
    def __init__(self):
        self.products = []

    def read_products_from_csv(filename='products.csv'):
        products = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            # Read each row and create a Product object
            for row in reader:
                product = Product.from_list_of_values_to_product_object(row)
                products.append(product)

        return products

    def write_products_to_csv(self, filename='products_PS1.csv'):
        writing = False
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            if not file_exists:
                writer.writerow(['product_id', 'name', 'price'])

            # Write each product as a row in the CSV
            for product in self.products:
                writer.writerow(product.product_object_to_list_of_individual_values())
                writing = True
        return writing

    def add_product(self, new_product):
        """
        add product object to products list
        
        input: new_product object
        
        return: boolean
        """
        if new_product in self.products:
            return False
        self.products.append(new_product)
        return True

    def list_products(self):
        """
        list all products
        
        return: if products exists in products list returns list
                else empty list
        """
        if self.products:
            return self.products
        return []

    def update_product(self, update_product):
        #product_id and price should be a object -> updated_product
        """
        update the price of given given input odjects id
        
        input: update_product object
        
        return: boolean
        
        """
        for product in self.products:
            if product.id == update_product.id:
                product.price = update_product.price
                return True
        return False

    def apply_discount(self, discount_percentage):
        """
        apply discount to all products
        
        input: int 
        
        return: if applied discount_percentage to all product's price 
                returns list of product, else returns empty list 
        """
        if self.products:
            for product in self.products:
                product.price = product.price - (product.price * (discount_percentage/100))
            return self.products
        return []
