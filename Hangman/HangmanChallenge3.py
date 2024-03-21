#----------STEP 2------#

# word_list = ["ardvark", "baboon", "camel"]

# guess = input("Guess a letter: ").lower()


# import random

# chosen_word = random.choice(word_list)
# print(chosen_word)

# display = []

# for letter in chosen_word:
#     if letter == guess:
#         x = guess
#     else:
#         x = "_"
#     display.append(x)
        
# print(display)

#------------STEP 3-----------#
# TO DO-1: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all
# the letters in the chosen_word and 'display' has no more blanks "_".
# Then you can tell the user they've won.


word_list = ["ardvark", "baboon", "camel"]

# guess = input("Guess a letter: ").lower()
import random

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for i in range(len(chosen_word)):
    display.append("_")
print(display)

while "_" in display:
    guess = input("Guess a letter: ")
    for l in range(len(chosen_word)):
        if chosen_word[l] == guess:
            display[l] = guess
    print(display)
    continue
while not "_" in display:
    print("You win!")
    break

# DONE
# Angela's way of doing it:
# word_length = len(chosen_word)

# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter: ")
    
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
    
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")