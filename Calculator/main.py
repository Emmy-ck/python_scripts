import os , time, sys
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return round((n1 / n2), 2)
def square(n1, n2):
    return round(n1 ** n2)

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': square
}

n1 = int(input("What is the first number?: "))
for sign in operations:
    print(sign)
    
operator = input("Pick an operation form the signs above: ")
n2 = int(input("What is the second number?: "))
if operator == '**':
    n2 = 2

calculator = operations[operator]
answer = calculator(n1, n2)
    
print(f"{n1} {operator} {n2} = {answer}")
choice = input("Do you want to continue? 'Y' for yes, 'N' to exit ").lower()
while choice == 'y':
    choice2 = input ("Type 'Y' to continue with math and 'N' to start new calculations: ").lower()
    if choice2 == 'y':
        operator = input("Pick another operator: ")
        n1 = answer
        n2 = int(input('What is the next number?: '))
        if operator == '**':
            n2 = 2
        calculator = operations[operator]
        answer = calculator(n1, n2)
    else:
        os.system('cls')
        os.system('python Day10/Calculator/main.py')
        n1 = int(input("What is the first number?: "))
        for sign in operations:
            print(sign)
    
        operator = input("Pick an operation form the signs above: ")
        n2 = int(input("What is the second number?: "))
        if operator == "**":
            n2 = 2

        calculator = operations[operator]
        answer = calculator(n1, n2)
    
    print(f"{n1} {operator} {n2} = {answer}")
    choice = input("Do you want to continue? 'Y' for yes, 'N' to exit ").lower()
    continue
    
else:
    print(".........................")
    time.sleep(3)
    os.system('cls')
    def bold(type):
        sys.stdout.write("\033[1m" + type + "\033[0m")
    bold('\t\tGoodbye!')
    time.sleep(5)
    os.system('cls')