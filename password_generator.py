# Password Generator Project
#----------------------------------------------------------------------------------------------------------#
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my PyPassword Generator!")
nr_letters = int(input('How many letters would you like in your password: \n'))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#----------------------------------------------------------------------------------------------------------#

word = []
for n in range(0, nr_letters):
    i = random.randint(0, len(letters))
    n = str(letters[i])
    word.append(n)
# print(word)

# sym = []
for x in range(0, nr_symbols):
    y = random.randint(0, len(symbols))
    x = str(symbols[y])
    word.append(x)
# print(word)

# num = []
for a in range(0, nr_numbers):
    b = random.randint(0, 10)
    a = str(b)
    word.append(a)
# print(word)
#------------PASSWORD SHUFFLE PART--------------#

new_word = random.sample(word, len(word)) #SHUFFLE
# print(new_word)
password = ''.join([str(x) for x in new_word])
print(f"Your password is: {password}") #COMBINE LIST IN ONE STRING

# DONE!!!!!! HARD LEVEL!!!!!!!
# Textbook solution:
# EASY LEVEL
password = ''

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    
print(password)

#HARD LEVEL

password_list = [] #convert it into a list instead of a string

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)

password = ''
for char in password_list:
    password += char
    
print(f'Your password is: {password}')