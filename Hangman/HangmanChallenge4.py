#-------------------- STEP 3 -------------------#

# word_list = ["ardvark", "baboon", "camel"]

# # guess = input("Guess a letter: ").lower()
# import random

# chosen_word = random.choice(word_list)
# print(chosen_word)

# display = []

# for i in range(len(chosen_word)):
#     display.append("_")
# print(display)

# while "_" in display:
#     guess = input("Guess a letter: ")
#     for l in range(len(chosen_word)):
#         if chosen_word[l] == guess:
#             display[l] = guess
#     print(display)
#     continue
# while not "_" in display:
#     print("You win!")
#     break

#------------------------- STEP 4 ----------------#

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TO DO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TO DO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#Join all the elements in the list and turn it into a String.

#TO DO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

word_list = ["ardvark", "baboon", "camel"]

# guess = input("Guess a letter: ").lower()
import random

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for i in range(len(chosen_word)):
    display.append("_")
print(f"{' '.join(display)}")

lives = len(stages)

while lives > 0:
  while "_" in display and lives > 0:
    guess = input("Guess a letter: ")
    for l in range(len(chosen_word)):
      if chosen_word[l] == guess:
        display[l] = guess
    if guess not in chosen_word: # Removing the if condition outside the for look ensures that the elements in the list are not popped repeatedly
      print(stages.pop()) # Hence we will ot be left with an empty list while iterating
      # print(stages.pop()) removes the last element in the list and prints it. 'Reverse append'
      lives = len(stages) # Re-assign the new length of the list after one element has been removed to a variable lives
    print(f"{' '.join(display)}")
    continue
  while "_" not in display:
    if lives == 1: # My addition to warn the user if one iteration (life) is left to break the loop
      print("Close call! You won!")
    else:
      print("You won!")
    break
  break
while lives == 0 and not lives < 0:
  if "_" in display:
    print("Game Over!")
    print(f'The word you were looking for is {chosen_word.upper()}')
    print("You lose")
  break

# DONE
# Angela's Solution:

# word_list = ["ardvark", "baboon", "camel"]

# # guess = input("Guess a letter: ").lower()
# import random
# end_of_game = False
# chosen_word = random.choice(word_list)
# print(chosen_word)
# word_length = len(chosen_word)

# lives = 6
# display = []

# for i in range(len(chosen_word)):
#     display.append("_")
# print(f"{' '.join(display)}")

# while not end_of_game:
#   for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#       display[position] = letter
#   if guess not in chosen_word:
#     lives -= 1
#     if lives == 0:
#       end_of_game = True
#       print("You lose!")
#   if "_" not in display:
#     end_of_game = True
#     print("You win!")
    
#   print(stages[lives])