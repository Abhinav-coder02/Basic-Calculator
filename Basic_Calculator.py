# A program that can perform arithmetic operations on two numbers

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to enter the operation (+, -, *, /)
op = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"The result is {result}")
