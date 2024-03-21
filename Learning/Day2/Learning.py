import random #import the built in random module
#------------------------------------------------------------------------------------------------#
#import my_module #import the module I created in a different file
#------------------------------------------------------------------------------------------------#
#randint(a, b) #generates a random integer between a and b(both inclusive).
#               This raises a ValueError if a > b

random_integer = random.randint(1, 100) #1 is start, 100 end, that's the range
print(random_integer)

#You can create your own modules and import them to a different file like this:
#1. Create a .py file with the name of the module(say my_module.py)
#2. Add all the variables and functions you will need inside my_module.py
#3. Use the function - import my_module - and the module will be implemented in the new file
#------------------------------------------------------------------------------------------------#
#print(my_module.pi) #usig the module 
#------------------------------------------------------------------------------------------------#

random_float = round(random.random(),5) #Generate random float betwee 1 and 100 but not including 1 and 100
#I have included the round funtion to round off to precise decimal places
print(random_float)



