#Write a program which will select a random name from the list of names.
#The person selected will have to pay everyone's food bill.
#You are ot allowed to use choice() function
#Line 10 splits the string names_string into individual names and puts them inside a List called names
#For it to work, you must enter all the names followed by comma then space
#Output : "{name} is going to buy the meal today!
# #Don't change the code below:
#-------------------------------------------------------------------------------------#
names_string = input("Give me everybody's name seperated by a comma. ")
names = names_string.split(", ") #split takes out the comma and space and converts every item to list format
#-------------------------------------------------------------------------------------#
import random

minimum_range = int(names.index(names[0])) #converts the first item to it's index 0 on the list. This determines the minimum of the range
maximum_range = int(names.index(names[-1])) #finds the maximum of the range by assigning the last item of the list to int of the index position of the item in the list

random_name = random.randint(minimum_range, maximum_range) #randomizes the items on the list

selected_name = (str(names[random_name])) #converts the random int to the string on the int index position
capital_first_letter = str.capitalize(selected_name) #converts the first letter of the string to capital letter

print(f"{capital_first_letter} is going to buy the meal today!") #prints the random name chosen
#we can ommit the f-string literal and concatenate i stead since the output is of the same type string
#print(capital_first_letter + " is going to by the meal today!")

#Done
#Another way of doing it:

names_string = input("Give me everybody's name seperated by a comma. ")
names = names_string.split(", ") #split takes out the comma and space and converts every item to list format

num_items = len(names) #get the total number of items in list

random_choice = random.randint(0, num_items - 1) #generate random numbrs between 0 and the last index

person_to_pay = names[random_choice]

print(person_to_pay + " is going to buy the meal today!")

#Another method using the choice() function:

names_string = input("Give me everybody's name seperated by a comma. ")
names = names_string.split(", ")

person_to_pay = random.choice(names)
print(person_to_pay + " is going to buy the meal today!")
