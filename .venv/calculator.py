on = True
def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)

def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)

def division():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)

while on:
    operation = input("Please enter +, -, *, / or Q ")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        division()
    elif operation == 'Q':
        on = False
    else:
        print("That operation is not available.")