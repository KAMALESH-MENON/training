def add_product(identifier, name, price, products):
    if identifier in products:
        print("identifier already exist")
    else:
        products[identifier] = {"name": name, "price": price}
        print(f"Product {name} added successfully\n")

def list_products(products):
    for identifier, value  in products.items():
        print(f"ID: {identifier}, Name: {value['name']}, Price: {value['price']}")

def update_product(identifier, name, price, products):
    if identifier not in products:
        print(f"\nproduct {identifier} does not exist")
    else:
        products[identifier]['name'] = name
        products[identifier]['price'] = price
        print(f"Product {identifier} updated successfully")

def apply_discount(discount_percentage, products):
    
    for identifier, value  in products.items():
        value["price"] -= value["price"]*(discount_percentage/100)
    print("\nListing Products after applying discount")

def start():
    products = {}
    add_product(1, "Product A", 100.0, products)
    add_product(2, "Product B", 150.0, products)
    list_products(products)
    update_product(3, "Product C",120.0, products)
    list_products(products)
    apply_discount(10, products)
    list_products(products)

start()