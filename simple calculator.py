def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error! Cannot divide by zero."
    return num1 / num2


def main():
    print("===== Simple Calculator =====")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result =", add(num1, num2))

    elif operator == "-":
        print("Result =", subtract(num1, num2))

    elif operator == "*":
        print("Result =", multiply(num1, num2))

    elif operator == "/":
        print("Result =", divide(num1, num2))

    else:
        print("Invalid operator!")


main()