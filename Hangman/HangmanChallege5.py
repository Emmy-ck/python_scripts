#------------- STEP 5 ----------------#
# TO DO-1: Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = [-----]
# TO DO-2: Import the stages from hangman_art.py and make this error go away.
# print(stages[lives])
# TO DO-3: Import the logo from the hangman_art.oy and print it at the start of the game
# TO DO-4: If the user has entered a letter they've already guessed, print the letter and let them know
# TO DO-5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word

# Importing modules
import random
from hangman_art import logo, stages
from hangman_words import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
lives = len(stages)
# print(chosen_word)

display = []
guessed_letters = []
for i in range(len(chosen_word)):
    display.append("_")
print(f"{' '.join(display)}")

reversed(stages)
lives = len(stages)

while lives > 0:
    while "_" in display and lives > 0:
        guess = input("Guess a letter: ")
        for l in range(len(chosen_word)):
            if chosen_word[l] == guess:
                display[l] = guess
                if guess in guessed_letters:
                    print(f"You already guessed {guess} correct.")
        if guess not in chosen_word:
            if guess in guessed_letters:
                print(f"You already guessed {guess}. That's not in the word. You lose a life")
            else:
                print(f"You guessed {guess} incorrect. You lose a life")
            print(stages.pop())
            lives = len(stages)
        print(f"{' '.join(display)}")
        guessed_letters.append(guess)
        continue
    while "_" not in display:
        if lives == 1:
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

# DONE!!!! With minimal effort