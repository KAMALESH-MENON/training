from product import Product
from order import Order
from logic import Logic

if __name__ == "__main__":
    o = Logic()

    # Create product objects
    product1 = Product(101, 'Mango', 40)
    product2 = Product(102, 'Apple', 25.99)
    product3 = Product(103, 'Plum', 15.49)
    product4 = Product(104, 'Kiwi', 12.99)

    # Save products to the database
    product1.save_to_db()
    product2.save_to_db()
    product3.save_to_db()
    product4.save_to_db()

    # Create order objects
    order1 = Order("order_1")
    order1.add_product(product1)
    order1.add_product(product2)
    order1.save_to_db()

    order2 = Order("order_2")
    order2.add_product(product2)
    order2.add_product(product3)
    order2.save_to_db()

    # Place orders
    o.place_order(order1)
    o.place_order(order2)

    # List orders
    print("All Orders:")
    for order in o.list_orders():
        print(order)

    # Calculate total cost
    total_cost = o.calculate_total_cost()
    if total_cost["calculation_status"]:
        print(f"\nTotal cost of all orders: {total_cost['total_cost']}")
    else:
        print("No products in orders")

    # Cancel an order
    o.cancel_order(order1)
    print("\nAfter cancelling order_1:")
    for order in o.list_orders():
        print(order)

    # Summarize orders
    summary = o.summarize_orders()
    if summary["summary_status"]:
        print("\nOrder Summary:")
        print(f"total_orders: {summary['total_orders']}, total_amount_spent: {summary['total_amount_spent']}, orders: {summary['orders']}")
    else:
        print("No products in orders")
