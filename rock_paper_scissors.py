import random

print("\n\tWelcome to a game of Rock, Paper, Scissors!\n\nDo you think you can beat the computer?")
start = input("\nDo you accept the challenge? y or n? ")

if start == 'y':
    print("Let's go!")
    
    rock = '''
        _________
    ---'     ____)
            (_____)
            (_____)
            (____)
    ---.____(___)'''
    paper = '''
        ______
    ---'   ___)___
            ______)
            ______)
            _____)
    ---.______)'''
    scissors = '''
        _______
    ---'    ___)____
                ____)_
            __________)
            (___)
    ---.____(__)'''

    print("Rules:\n\tEnter 0 for Rock.\n\tEnter 1 for Paper.\n\tEnter 2 for Scissors.")
    print("\n\tROCK, PAPER, SCISSORS, GO!\n")
    computer_choice = random.randint(0, 2)
    player = int(input("0, 1 or 2? "))

    if player == 0:
        print(f"You picked Rock \n {rock}")
        if computer_choice == 1:
            print(f"Computer picked Paper \n {paper}")
            print('\n\tPaper beats rock \n\t YOU LOSE!')
        elif computer_choice == 2:
            print(f"Computer picked Scissors \n {scissors}")
            print("\n\tRock beats Scissors.\n\tYOU WIN!")
        else:
            print(f"Computer picked Rock \n {rock}")
            print("\n\tDRAW")
    elif player == 1:
        print(f"You picked Paper \n {paper}")
        if computer_choice == 2:
            print(f"Computer picked Scissors \n {scissors}")
            print('\n\tScissors beat Paper \n\t YOU LOSE!')
        elif computer_choice == 0:
            print(f"Computer picked Rock \n {rock}")
            print("\n\tPaper beats Rock.\n\tYOU WIN!")
        else:
            print(f"Computer picked Paper \n {paper}")
            print("\n\tDRAW")
    elif player == 2:
        print(f"You picked Scissors \n {scissors}")
        if computer_choice == 0:
            print(f"Computer picked Rock \n {rock}")
            print('\n\tRock beats Scissors \n\t YOU LOSE!')
        elif computer_choice == 1:
            print(f"Computer picked Paper \n {paper}")
            print("\n\tScissors beats Paper.\n\tYOU WIN!")
        else:
            print(f"Computer picked Scissors \n {scissors}")
            print("\n\tDRAW")
    else:
        print("Error: Invalid Input")
elif start == 'n':
    print("\n\tGoodbye!")
else:
    print("Invalid input")