# Simple command-line calculator using only if-else

print("Welcome to Simple Calculator!")

while True:
    first_input = input("\nEnter first number (or 'exit' to quit): ").strip()
    if first_input.lower() == 'exit':
        print("Goodbye!")
        break
    elif first_input.lower() == 'clear':
        print("Cleared.")
        continue

    # Validate first number
    try:
        a = float(first_input)
    except ValueError:
        print("Invalid number! Please enter a valid number.")
        continue

    operator = input("Enter operator (+, -, *, /): ").strip()
    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator! Please enter +, -, *, or /.")
        continue

    second_input = input("Enter second number: ").strip()
    try:
        b = float(second_input)
    except ValueError:
        print("Invalid number! Please enter a valid number.")
        continue

    # Calculation using if-else only
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            print("Error: Cannot divide by zero!")
            continue
        result = a / b

    print(f"Result: {result}")