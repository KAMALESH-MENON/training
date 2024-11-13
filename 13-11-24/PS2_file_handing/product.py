class Product:
    """A class to handle product functionality."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"[product id: {self.product_id}, name: {self.name}, price:{self.price}]"

    def product_object_to_list_of_individual_values(self):
        return [self.product_id, self.name, self.price]

    @classmethod
    def from_list_of_values_to_product_object(cls, row_from_csv_read_function):
        return cls(int(row_from_csv_read_function[0]), row_from_csv_read_function[1], float(row_from_csv_read_function[2]))
