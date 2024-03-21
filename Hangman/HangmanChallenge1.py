#Step 1

word_list = ["ardvark", "baboon", "camel"]

#ToDo-1 - Randomly chose a word from the word_list
# and assign it to a variable called chosen_word.

#ToDo-2 - Ask the user to guess a letter and assign their answer
# to a variable called guess. Make the guess  lowercase.

#ToDo-3 - Check f the letter the user has guessed (guess)
# is one of the letters in the chosen_word.
import random
# Prints the word at the chosen random index with range 0 to last item of the list
word = word_list[random.randint(word_list.index(word_list[0]), word_list.index(word_list[-1]))]
chosen_word = list(word.strip(''))

guess = input('Guess a letter: ').lower()
print(chosen_word)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print('Wrong')

#Done
# You can also make the code simpler by using the random.choice() function
# Used this way: chosen_word = random.choice(word_list)

