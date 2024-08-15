import os, time, math, random
from art import logo

# Cards in the deck in form of a list
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Create an empty list to represent an empty hand at the start of the game
player_cards = random.sample(cards,2)
computer_cards = random.sample(cards,2)

# Creating global variables for the total points each player has
player_total = sum(player_cards)
comp_total = sum(computer_cards)

def game():
    """Function that determines the winner of a Black Jack game depending on the total points of a player and a dealer

    The function compares the player's total points ('player_total') and the dealer's points ('comp_total')
    
    The function assumes the player_total and comp_total are defined globally
    """
    if player_total <= 21 and comp_total <= 21:
        if player_total > comp_total:
            print("You Win!")
        elif player_total < comp_total:
            print("Dealer Wins!")
        else:
            print('Draw')
                
    elif player_total > 21 and comp_total <= 21:
        print("Dealer Wins!")
    elif player_total < 21 and comp_total >= 21:
        print("Player Wins!")
    elif player_total > 21 and comp_total > 21:
        print("You Both Lose!")

if (input("Do you want to play a game of Black Jack? 'y' or 'n': ").lower()) == 'y':
    print(logo)
    print(f'Your cards: {player_cards} Your total: {player_total}')
    print(f'Dealer\'s first card: [{computer_cards[0]}]')
    if (input("Type 'y' to get another card, 'n' to pass: ".lower())) == 'y':
        player_cards.extend(random.sample(cards,1))
        player_total = sum(player_cards)
        print(f'Your cards : {player_cards} Your total: {player_total}')
        if comp_total <= 17:
            computer_cards.append(int(''.join([str(x) for x in random.sample(cards,1)])))
        comp_total = sum(computer_cards)
        print(f'Dealer\'s cards : {computer_cards} Dealer total: {comp_total}')
        game()
    else:
        print("You have passed your turn")
        print("Dealer\'s Turn: ")
        computer_cards.append(int(''.join([str(x) for x in random.sample(cards,1)])))
        print(f'Dealer\'s cards: {computer_cards} Dealer\'s total: {comp_total}')
        game()
else:
    print("Too bad, Goodbye!")
    
# os.system('python Day11/BlackJack/main.py')