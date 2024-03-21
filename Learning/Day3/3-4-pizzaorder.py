#Build an automatic pizza order program
#Based on the user's input, work out the final bill
#Small Pizza : $15
#Medium Pizza : $20
#Large Pizza : $25
#Pepperoni for Small pizza : +$2
#Pepperoni for Medium or Large : +$3
#Extra cheese for any size pizza : +$1 
#Don't change the code below
#---------------------------------------------------------------------#
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#---------------------------------------------------------------------#
bill_small = 15
bill_medium = 20
bill_large = 25

if size == "S":
    if add_pepperoni == "Y":
        bill_small += 2
        if extra_cheese == "Y":
            bill_small += 1
            print(f"Your total bill is: ${bill_small}")
        else:
            print(f"Your total bill is: ${bill_small}")
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            bill_small += 1
            print(f"Your total bill is: ${bill_small}")
        else:
            print(f"Your total bill is: ${bill_small}")
elif size == "M":
    if add_pepperoni == "Y":
        bill_medium += 3
        if extra_cheese == "Y":
            bill_medium += 1
            print(f"Your total bill is: ${bill_medium}")
        else:
            print(f"Your total bill is: ${bill_medium}")
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            bill_medium += 1
            print(f"Your total bill is: ${bill_medium}")
        else:
            print(f"Your total bill is: ${bill_medium}")
elif size == "L":
    if add_pepperoni == "Y":
        bill_large += 3
        if extra_cheese == "Y":
            bill_large += 1
            print(f"Your total bill is: ${bill_large}")
        else:
            print(f"Your total bill is: ${bill_large}")
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            bill_large += 1
            print(f"Your total bill is: ${bill_large}")
        else:
            print(f"Your total bill is: ${bill_large}")
else:
    print("Invalid input")
    
#Done
#Another solution:

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}")