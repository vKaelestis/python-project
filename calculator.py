def calculator():
    x = input("Enter the first number: ")
    y = input("Enter the operator: ")
    z = input("Enter the second number: ")

    try:
        x = float(x)
        z = float(z)    
    except ValueError:
        print("Error: Please enter valid numbers.")
        return
    
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        if float(z) != 0:
            return float(x) / float(z)
        else:
            raise ValueError("Error: Division by zero is not allowed")
    else:
        raise ValueError("invalid operator")


result = calculator()
if result is not None:
    print(f"Result: {result}")

