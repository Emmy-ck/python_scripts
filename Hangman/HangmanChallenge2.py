
#----------STEP 2------#

word_list = ["ardvark", "baboon", "camel"]

#TO DO 1: - Create an empty list called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was 'Apple', display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess

guess = input("Guess a letter: ").lower()

# TO DO-2: Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen_word was "apple", then display should be ["_", "p", "p","_","_",].

# TO DO-3: Print 'display' and you should see the guessed letter in the correct position and every other letter replaced with "_".

# Hint - Don't worry about getting the user to guess the next letter, We'll tackle that in step 3.

import random

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
# for letter in range(len(chosen_word)):
#     display.append("_")
# print(display)

for letter in chosen_word:
    if letter == guess:
        x = guess
    else:
        x = "_"
    display.append(x)
        
print(display)

# DONE
# Another way of doing it:

display = []

for _ in range(len(chosen_word)):
    display += "_"
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter