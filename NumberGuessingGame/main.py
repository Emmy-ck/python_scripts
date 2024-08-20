import os, random, time
from art import logo
from random import randint

prompt = str(input("Would you like to play a game of Guess The Number? 'y' or 'n': ").lower())
while (prompt != 'y') and (prompt != 'n'):
    print("Invalid input. Type 'y' or 'n':")
    prompt = str(input("Would you like to play a game of Guess The Number? 'y' or 'n': ").lower())
    if prompt == "n":
        print("Goodbye!")
        os.system("cls")
        break

comp_choice = int(random.randint(1, 101))
print(f"Computer choice is {comp_choice}")

# print(logo)
def guess_the_number():
    """Initiates number guessing game where player tries to guess correctly a randomly generated number

    Returns:
        bool: True if correct number, False if the guess is wrong
    """
    if prompt == 'y':
        print(logo)
        level = str(input("Pick a level. Type 'easy' or 'hard': ").lower())
        
        # Prompts the user to type the level accurately
        while (level != 'easy') and (level != 'hard'):
            print("Invalid input. Try again")
            level = str(input("Pick a level. Type 'easy' or 'hard': ").lower())
            if (level == 'easy') or (level == 'hard'):
                break

        if level == 'easy':
            attempts = 10
            print(f"\t\t\tEasy level. \n\tYou have {attempts} attempts to guess the correcct number.\n\t\t\tALL THE BEST!")

        else:
            attempts = 5
            print(f"\t\t\tHard level. \n\tYou have {attempts} attempts to guess the correct number.\n\t\t\tALL THE BEST!")

        while True:
            player_choice = int(input("Pick a number between 1 and 100: "))
            if (player_choice in range(1,101)) and (comp_choice in range(1,101)):
                while player_choice != comp_choice:
                    attempts -= 1
                    if attempts <= 0:
                        print("Out of attempts! You lose!")
                        print(f"The number was {comp_choice}")
                        break
                # player_choice == comp_choice:
                # print (f'CONGRATULATIONS! You guessed {comp_choice} correct!')
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
    return

guess_the_number()