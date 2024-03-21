#Write a program that tests the compatibility between two people
#Use the super scientific methos recommended by BuzzFeed:
#Take both people's names and check for the number of times the letters in the word TRUE occurs.
#Then check for the number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number
#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is x, you go together like coke and mentos."
#For scores between 40 and 50:
#"Your score is y, you are alright together."
#Otherwise: "Your score is z."
#Don't change the code below
#-----------------------------------------------------#
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#-----------------------------------------------------#

name1 = str.lower(name1) #converts the string to lowercase
name2 = str.lower(name2)

names = name1 + name2 #concatnates the two names and stores in new variable names

n = names.count("t") + names.count("r") + names.count("u") + names.count("e")
m = names.count("l") + names.count("o") + names.count("v") + names.count("e")
#Takes the number of times the letters appear in the combined string and sums the count.
#The count is stored in a new variables n and m

n = str(n)
m = str(m) #converts the counts to strings for concatnation

lovescore = int(n + m) #combines the values in a new variable 'lovescore' and converts to int type

if (lovescore < 10) or (lovescore > 90):
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif (lovescore >= 40) and (lovescore <= 50):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")
    
#Done
#Another solution is:

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")