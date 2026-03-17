
def calculate(num1, num2, operator):
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operator"

    return result



a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

answer = calculate(a, b, op)


print("Result =", answer)
