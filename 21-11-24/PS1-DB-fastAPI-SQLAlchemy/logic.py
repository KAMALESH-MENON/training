from config import SessionLocal, get_db
from product import Product
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

class Logic:
    def __init__(self):
        self.db = SessionLocal()

    def add_product(self, new_product):
        try:
            self.db.add(new_product)
            self.db.commit()
            return True
        except IntegrityError:
            self.db.rollback()
            return False

    def list_products(self):
        return self.db.query(Product).all()

    def update_product(self, update_product):
        db_product = self.db.query(Product).filter(Product.id == update_product.id).first()
        if db_product:
            db_product.price = update_product.price
            self.db.commit()
            return True
        return False

    def apply_discount(self, discount_percentage):
        products = self.list_products()
        for product in products:
            product.price -= product.price * (discount_percentage / 100)
            self.update_product(product)
        return self.list_products()
