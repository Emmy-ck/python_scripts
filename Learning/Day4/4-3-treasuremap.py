#Write a program that will mark a spot with an x
#The ap is made of 3 rows of blank squares
#Your program should allow you to enter the position of the treasure using a two-digit system.
#The first digit is the vertical column number
#The second digit is the horizintal row number
#Don't change the code below:
#--------------------------------------------------------------------------------#
row1 = [" || ", " || ", " ||"]
row2 = [" || ", " || ", " ||"]
row3 = [" || ", " || ", " ||"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#--------------------------------------------------------------------------------#

position = int(position)

if position == 11:
    row1[0] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 12:
    row1[1] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 13:
    row1[2] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 21:
    row2[0] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 22:
    row2[1] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 23:
    row2[2] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 31:
    row3[0] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 32:
    row3[1] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
elif position == 33:
    row3[2] = ' X '
    print(f"{row1}\n{row2}\n{row3}")
else:
    print("Invalid input")
    
#Done
#A simpler way of doing it:

row1 = [" || ", " || ", " ||"] 
row2 = [" || ", " || ", " ||"]
row3 = [" || ", " || ", " ||"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) #Takes the input and stores the first value to variable horizontal
vertical = int(position[1]) #Takes the input and stores the second number to variable vertical

selected_row = (map[vertical - 1]) #Takes the second digit of the position and selects the row to change
selected_row[horizontal - 1] = "X" #Takes the index of the selected row to change and changes the value to "X"

#The two lines above can also be combined to one line as shown below:
map[vertical - 1][horizontal - 1] = "X"
