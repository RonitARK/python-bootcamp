
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, **, //): ")

if operation == "+":
    result = print("num1 + num2 = ", num1 + num2)
elif operation == "-":
    result = print("num1 - num2 = ", num1 - num2)
elif operation == "*":
    result = print("num1 * num2 = ", num1 * num2)
elif operation == "/":
    if num2 != 0:
        result = print("num1 / num2 = ", num1 / num2)
    else:
        result = print("Error: Division by zero is not allowed.")
elif operation == "%":
    if num2 != 0:
        result = print("num1 % num2 = ", num1 % num2)
    else:
        result = print("Error: Division by zero is not allowed.")
elif operation == "**":
    result = print("num1 ** num2 = ", num1 ** num2)
elif operation == "//":
    if num2 != 0:
        result = print("num1 // num2 = ", num1 // num2)
    else:
        result = print("Error: Division by zero is not allowed.")
