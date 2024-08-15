import os, random, time
from art import logo
from random import randint

comp_choice = random.randint(1, 100)
player_choice = int(input('Select a number: '))

def scale(player_choice, comp_choice):
    """Compares the player's guess with the computer's chosen number.

    Args:
        player_choice (int): Number guessed by the player.
        comp_choice (int): Number the computer selected to be guessed.

    Returns:
        str: A message indicating whether the guess is too high, too low, or correct.
    """
    if player_choice == comp_choice:
        print (f'CONGRATULATIONS! You guessed {comp_choice} correct!')
    elif player_choice < comp_choice:
        print ('Too low!')
    else:
        print ('Too high!')

scale(player_choice=int,comp_choice=int)

print(f"Computer choice is {comp_choice}")
print(f'Your choice is {player_choice}')