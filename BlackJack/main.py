import os, time, math, random
from art import logo

# Import the art from file art.py
print(logo)

# Cards in the deck in form of a list
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Create an empty list ti represent an empty hand at the start of the game
player_cards = []
computer_cards = []

player_total = sum(player_cards)
comp_total = sum(computer_cards)

def black_jack(player_total, comp_total):
    