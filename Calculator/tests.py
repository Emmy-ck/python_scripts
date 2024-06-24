import os
from art import logo

print(logo)

n1 = int(input("What is the first number?: "))
signs = ['+',"-","*","/"]
for sign in signs:
    print(sign)
operator = input("Pick an operator: ")
n2 = int(input("What is the next number?: "))

def add(n1, n2):
    return int(n1 + n2)
def subtract(n1, n2):
    return int(n1 - n2)
def multiply(n1, n2):
    return int(n1 * n2)
def divide(n1, n2):
    return round((n1/n2), 2)

calculator_record = {
    add : '+',
    subtract : '-',
    multiply : '*',
    divide : '/',
}

def calculator():
    if operator == '+':
        result = add(n1,n2)
    elif operator == '-':
        result = subtract(n1,n2)
    elif operator == '*':
        result = multiply(n1,n2)
    elif operator == '/':
        result = divide(n1,n2)
    else:
        print('Invalid Operator. Try again')
        os.system('cls')
    print(f"{n1} {operator} {n2} = {result}")
    new_math = input(f"Type 'y' to continue with {add(n1,n2)}, or 'n' to start new calculation: ")
    while new_math == 'Y':
        n1 = int (result)
        n2 = int(input("What is the next number?: "))
        operator = input("Pick an operator: ")
        calculator()
    if new_math == 'n':
        os.system('cls')
        os.system('python Day10/Calculator/tests.py')
    else:
        print('Invalid entry')
        os.system('python Day10/Calculator/tests.py')

calculator()