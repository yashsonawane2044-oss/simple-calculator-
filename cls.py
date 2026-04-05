# Simple Command-Line Calculator

def calculate(num1, num2, operator):
    """Perform calculation based on the operator."""
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Invalid number"
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Unknown operator"

def main():
    while True:
        print("\nSimple Calculator")
        print("Enter 'exit' to quit or 'clear' to reset.\n")
        
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            break
        if num1.lower() == 'clear':
            continue
        
        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            break
        if operator.lower() == 'clear':
            continue
        
        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            break
        if num2.lower() == 'clear':
            continue
        
        result = calculate(num1, num2, operator)
        print("Result:", result)

if __name__ == "__main__":
    main()