import random

# Constants for production rates


# Variable to track quality checks
quality_pass_rate = 0.9

# Function to simulate production
def produce_products(hours, production_rates, inventory):
    for hour in range(1, hours + 1):
        print(f"Hour {hour}:")
        for product, rate in production_rates.items():
            produced = rate  # number of products produced in one hour
            inventory[product] += produced
            print(f"Produced {produced} units of Product {product}. Current inventory: {inventory[product]}")

# Function to monitor inventory
def monitor_inventory(threshold, inventory):
    print("\nMonitoring inventory:")
    for product in inventory:
        if inventory[product] < threshold:
            print(f"Inventory of Product {product} is below threshold. Current inventory: {inventory[product]}")
            inventory[product] += 1  # simulate additional production
            print(f"Added 1 unit to Product {product}. Current inventory: {inventory[product]}")

# Function to perform quality checks
def quality_check(inventory):
    print("\nQuality check process:")
    quality_check_passed = {}
    for product in inventory:
        quality_check_passed[product] = []
        for item in range(inventory[product]):
            if random.random() < quality_pass_rate:
                quality_check_passed[product].append('Pass')
            else:
                quality_check_passed[product].append('Fail')
    return quality_check_passed

# Function to summarize quality check results
def summarize_quality_checks(quality_results):
    print("\nQuality check results:")
    for product, results in quality_results.items():
        passed = results.count('Pass')
        failed = results.count('Fail')
        print(f"Product {product}: Passed {passed}, Failed {failed}")

# Main function to run the manufacturing simulation
def run_manufacturing_simulation():
    production_rates = {
        'A': 5,  # products per hour
        'B': 3,
        'C': 4
    }

    # Initial inventory
    inventory = {
        'A': 0,
        'B': 0,
        'C': 0
    }
    
    total_hours = 8
    threshold = 30

    # Produce products
    produce_products(total_hours, production_rates, inventory)

    # Monitor inventory
    monitor_inventory(threshold, inventory)

    # Perform quality checks
    quality_results = quality_check(inventory)

    # Summarize quality checks
    summarize_quality_checks(quality_results)

    # Final inventory summary
    print("\nFinal Inventory Summary:")
    for product, count in inventory.items():
        print(f"Product {product}: {count} units")

# Run the simulation
if __name__ == "__main__":
    run_manufacturing_simulation()
