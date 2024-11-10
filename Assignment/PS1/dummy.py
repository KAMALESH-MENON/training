"dummy file for testing"
from logic import Logic
from product import Product

if __name__ == "__main__":
    l1 = Logic()

    p1 = Product(1, "Milk", 45)
    p2 = Product(2, "Notebook", 50)

    l1.add_product(p1)
    l1.add_product(p2)
    S = l1.update_product(2, 55)
    l1.apply_discount(10)
    list_of_products = l1.list_products()
    for Product in list_of_products:
        print(Product)