## Functions

# Function definition and calling
def function_name():
    # Code block (body of function)
    print("Hello, this is a function!")

def emptygreet():
    print("Hello, welcome to class!")

emptygreet()

# Adding two numbers through function
def add(a, b):  # This is an example of a function that returns a value
    return a + b

result = add(3, 5)
print(result)

def Addition(a, b):  # This is an example of the same function and prints the result
    result = a+b
    print(result)

Addition(2,4)


# check if the number is even
def check_even(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check_even(4)
check_even(7)

# check if the number is positive
def is_positive(num):
    return num > 0

num = int(input("Enter a number: "))
print(is_positive(num))   # True
print(is_positive(-3))  # False

# Function with default parameter
# Default parameter allows a function to be called with fewer arguments than it is defined to accept.
def defaultgreet(name="Student"):
    print("Hello", name)

defaultgreet()         # Uses default: Student
defaultgreet("Sarah")  # Uses given name

# Function with no default parameters
def greet(name):
    print("Hello", name, "welcome!")

greet("Ali")
greet("Aisha")

# find the max number
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Max is:", find_max(10, 3))

# Printing Stars
def print_stars(n):
    # for i in range(n):
    print("hello" * n)

print_stars(5)



'''
Project Task: Create a simple calculator app that can perform addition, subtraction, multiplication, and division.
- The app should run indefinitely until the user chooses to exit.
- The user should be able to input two numbers and select an operation.
- All operations should be implemented as separate functions.
- The app should handle invalid inputs as well
'''
## Simple Calculator App

# Basic operation functions
def addition(c, d):
    result = c + d
    return result

def subtraction(c, d):
    result = c - d
    return result

def multiplication(c, d):
    result = c * d
    return result

def division(c, d):
    result = c / d
    return result

# Main function to run the calculator
def calculator():
    c = int(input("enter number 1: "))
    d = int(input("enter number 2: "))
    operation = int(input("Enter 1 for Addition, Enter 2 for subtraction, Enter 3 for multiplication, Enter 4 for division " \
    "Enter 0 to exit: "))

    if operation == 0:
        return False
    elif operation == 1:
        print(addition(c,d))
    elif operation == 2:
        print(addition(c,d))
    elif operation == 3:
        print(addition(c,d))
    elif operation == 4:
        print(addition(c,d))
    else:
        print("Wrong operation")

# Loop to keep the app running
while True:
    flag = calculator()
    if flag == False:
        break