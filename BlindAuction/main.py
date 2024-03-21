"""
Blind Auction Program

This program simulates a blind auction where participants can submit bids without knowing the bids of other participants.
The auction is conducted in a way that keeps the bids confidential until the end of the bidding period.

Usage:
1. Run the program.
2. Participants can enter their name and submit their bids.
3. The program reveals the winner and the winning bid.

"""
import os
from art import logo

print(logo)
print("Blind Auction Program")
bidders = {}

player = input("What is your name? ")
bid = int(input("What is your bid? $ "))
os.system('cls')

bidders[player] = bid

exit_bid = input("Next player bid? Y/N").lower()

while exit_bid == "y":
    player = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    os.system('cls')
    
    bidders[player] = bid
    
    exit_bid = input("Next player bid? Y/N ").lower()
    
    if exit_bid == "n":
        break
    
max_bid = 0
for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]

for key, value in bidders.items():
    if value == max_bid:
        winner = key
        
print(f"{winner} won with a bid of $ {max_bid}")
print("Close of Blind Auction. Thank you!")

os.system('cls') # Clears the terminal automatically

# Also learnt how to ru the program automatically from my python script -->
# os.system('python Day9/BlindAuction/main.py')

# Another solution

# from replit import clear
# from art import logo
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()