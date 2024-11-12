from order import Order
from product import Product

if __name__ == "__main__":
    p1 = Product(1, "Milk", 45)
    p2 = Product(2, "Mango", 30)
    o1 = Order(1)
    temp = o1.add_product_in_orders()
    temp = o1.add_product(1, p2)
    o2 = Order(2)
    o2.add_product(2, p2)
    o2.delete_order(1)
    print(o2)