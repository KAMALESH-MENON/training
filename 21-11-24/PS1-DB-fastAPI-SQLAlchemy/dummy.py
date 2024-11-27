"dummy file for testing"
from logic import Logic
from product import Product
from config import engine, Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    l1 = Logic()

    p1 = Product(id=1, name="Milk", price=45)
    p2 = Product(id=2, name="Notebook", price=50)

    res1 = l1.add_product(p1)
    print("added product p1 =", res1)
    
    res2 = l1.add_product(p2)
    print("added product p2 =", res2)

    up1 = Product(id=1, name="Milk", price=55)
    update_res = l1.update_product(up1)
    print("updated product up1 =", update_res)

    discount_percentage = 10
    discounted_products = l1.apply_discount(discount_percentage)
    print("discounted products:")
    for product in discounted_products:
        print(product)

    list_of_products = l1.list_products()
    print("list of products after discount:")
    for product in list_of_products:
        print(product)
