#This is a simple calculator program that takes two numbers and an operation from the user and performs the calculation.

a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
operation= input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
print("The result is:", result)
