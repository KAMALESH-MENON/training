import Logic


def main():
    print("Welcome to the Simple Calculator!")
    
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nSelect the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    
    choice = input("Enter the choice (1/2/3/4): ")

    
    if choice == '1':
        result = Logic.add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = Logic.subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = Logic.multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = Logic.divide(num1, num2)
        operation = "Division"
    else:
        result = "Invalid choice!"
        operation = ""

    
    if operation:
        print(f"\nResult of {operation}: {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()