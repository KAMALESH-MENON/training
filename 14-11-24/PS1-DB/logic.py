from db import db_connection
from product import Product
import sqlite3

class Logic:
    """logic part of PS1"""
    def __init__(self):
        self.connection = db_connection()

    def add_product(self, new_product):
        """
        Add product object to products list
        
        Input: new_product object
        
        Return: boolean
        """
        try:
            with self.connection:
                self.connection.execute(
                    'INSERT INTO products (id, name, price) VALUES (?, ?, ?)',
                    (new_product.id, new_product.name, new_product.price)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def list_products(self):
        """
        List all products
        
        Return: list of products or empty list
        """
        cursor = self.connection.execute('SELECT id, name, price FROM products')
        products = [Product(row[0], row[1], row[2]) for row in cursor.fetchall()]
        return products

    def update_product(self, update_product):
        """
        Update the price of the given product
        
        Input: update_product object
        
        Return: boolean
        """
        with self.connection:
            cursor = self.connection.execute(
                'UPDATE products SET price = ? WHERE id = ?',
                (update_product.price, update_product.id)
            )
            return cursor.rowcount > 0

    def apply_discount(self, discount_percentage):
        """
        Apply discount to all products
        
        Input: discount_percentage as int
        
        Return: list of products after applying discount or empty list
        """
        products = self.list_products()
        for product in products:
            product.price -= product.price * (discount_percentage / 100)
            self.update_product(product)
        return products
