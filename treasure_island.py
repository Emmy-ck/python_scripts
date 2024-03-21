print("\n\tWELCOME TO TREASURE ISLAND!")
print("\nYour mission is to find the treasure.\n")
print("\nHow to play:\n\tFollow the clues to the treasure.\n\t\tGOOD LUCK!")

player = "Player 1"
player = input("Enter your name to start: ")

player = str.upper(player)
print("\n\tLet's go " + player + "!")

path = input("\nThere are two paths ahead of you. Which one will you take? Right or Left? ")
path = str.lower(path)

if path == "left":
    print("\n\tRight choice! You have found a map to the island.")
    print("\n\nYou are at a shore and the boat that should take you to the island will arrive in 3 hours.\nYou are standing at the edge of the jungle and it's getting dark.")
    action = input("\n\tWhat will you do? Swim or Wait? ")
    action = str.lower(action)
    
    if action == "wait":
        print("\n\tRight choice again!\n\nYou find an abandoned house nearby.\n\nYou can get supplies and shelter while you wait.")
        print("The house has 3 doors and you have to choose the right door to go through.\n\n\tChoose wisely!")
        door = input("\n\tWhich door will you choose? Blue, Red, Yellow? ")
        door = str.lower(door)
        
        if door == "yellow":
            print("\n\t\tCONGRATULATIONS!!!\n\tYou found the treasure! Great!\n\t\tYOU WIN!!")
        elif door == "red":
            print("\n\tOops! You walked into a room with a deadly virus!!\n\t\tGAME OVER!")
        else:
            print("\n\tOops! You were captured by pirates!\n\t\tGAME OVER!")
        
    else:
        print("\n\tOMG! There are sharks in the water!\n\t\tGAME OVER!")
else:
    print("\n\tOops! You fell into a hole.\n\t\tGAME OVER!")
    
#Done

