#Write a virtual coin toss program that randomly tells the user "Heads" or "Tails".
#First letter should be capitalized and spelled exactly like in the example

import random

print("Coin Toss Program")

random_int = random.randint(0,1)

if random_int == 0:
    print("Heads")
else:
    print("Tails")
    
#Done