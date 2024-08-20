import os
import random
import time
from art import logo
from random import randint

# Ask users if they want to play the game
prompt = str(input("Would you like to play a game of Guess The Number? 'y' or 'n': ").lower())

# Loop to esure valid input for starting the game
while (prompt != 'y') and (prompt != 'n'):
    print("Invalid input. Type 'y' or 'n':")
    prompt = str(input("Would you like to play a game of Guess The Number? 'y' or 'n': ").lower())

    # If the player doesn't want to play
    if prompt == "n":
        print("Goodbye!")
        os.system("cls") # Clears the terminal/command line screen
        break

# Generate computer's random choice between 1 and 100
comp_choice = int(random.randint(1, 101))
# print(f"Computer choice is {comp_choice}") # For debugging purposes

# Define the main game function
def guess_the_number():
    """Initiates number guessing game where player tries to guess correctly a randomly generated number

    Returns:
        None: The function returns nothing. It runs the game till the player wins or loses
    """
    
    # If the player chooses to play the game
    if prompt == 'y':
        print(logo) # Display the game logo
        
        # Asks the player to choose a difficulty level
        level = str(input("Pick a level. Type 'easy' or 'hard': ").lower())
        
        # Ensure valid input for difficulty level
        while (level != 'easy') and (level != 'hard'):
            print("Invalid input. Try again")
            level = str(input("Pick a level. Type 'easy' or 'hard': ").lower())
            if (level == 'easy') or (level == 'hard'):
                break

        # Set the number of attempts based on the difficulty level
        if level == 'easy':
            attempts = 10
            print(f"\t\t\tEasy level. \n\tYou have {attempts} attempts to guess the correcct number.\n\t\t\tALL THE BEST!")

        else:
            attempts = 5
            print(f"\t\t\tHard level. \n\tYou have {attempts} attempts to guess the correct number.\n\t\t\tALL THE BEST!")

        # Start the guessing loop
        while True:
            player_choice = int(input("Pick a number between 1 and 100: "))
            if (player_choice in range(1,101)) and (comp_choice in range(1,101)):
                while player_choice != comp_choice:
                    attempts -= 1
                    if attempts <= 0:
                        print("Out of attempts! You lose!")
                        print(f"The number was {comp_choice}")
                        break
                    if player_choice < comp_choice:
                        print ('Too low!')
                        player_choice = int(input("Pick another number: "))
                    elif player_choice > comp_choice:
                        print ('Too high!')
                        player_choice = int(input("Pick another number: "))
                else:
                    print(f"CONGRATULATIONS! You guessed {comp_choice} correct!")
                    break
            else:
                print("Invalid choice! Number out of range.")
                player_choice = int(input("Pick another number: "))
    return # Exit the function after the game ends

# Start the game by calling the name function
guess_the_number()