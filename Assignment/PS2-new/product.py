class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def __str__(self):
        return f"[product id: {self.product_id}, name: {self.name}, price:{self.price}]"
    def __repr__(self):
        return f"Product({self.product_id}, '{self.name}', {self.price})"

products = [
    Product(101, 'Widget', 19.99),
    Product(102, 'Gadget', 25.99),
    Product(103, 'Doodad', 15.49),
    Product(104, 'Thingamajig', 12.99),
    Product(105, 'Whatsit', 22.49)
]
