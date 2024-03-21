#Write a program that works out whether a year is a leap year.
#A normal year has 365 days
#Leap years have 366 days with an extra day in February.
#Don't chage the code below:
#----------------------------------------------------------#
year = int(input("Which year do you want to check? "))
#----------------------------------------------------------#

if ((year % 4) == 0) and ((year % 100) != 0):
    print(f"{year} is a Leap year")
elif ((year % 100) == 0) and ((year % 400) == 0):
    print(f"{year} is a Leap year")
elif ((year % 100) == 0) and ((year % 400) != 0):
    print(f"{year} is Not a Leap year")
else:
    print(f"{year} is Not a Leap year")

#Done
#Here's another way of solvig it

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")