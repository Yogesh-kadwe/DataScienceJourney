# Program 1
# Handle division by zero.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1/num2)
except Zerodivisiorerror:
    print("Cannot divide by zero")


try:
    age=int(input("Enter age: "))
    print(f"Age : {age}")
except ValueError:
    print("Please enter a valid number")


