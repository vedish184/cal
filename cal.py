# calculator.py
def main():
    print("Calculator program!")
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print("Choose an operation: ")
        print("1. Subtraction")
        print("2. Multiplication")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print(f"The result of subtraction: {n1 - n2}")
        elif choice == "2":
            print(f"The result of multiplication: {n1 * n2}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter numeric values.")

if __name__ == "__main__":
    main()
