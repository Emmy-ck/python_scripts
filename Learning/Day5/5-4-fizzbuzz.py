# Write a program that automatically prints the solution to the FizzBuzz game.
# The program should print each umber from 1 to 100 in turn.
# When the number is divisible by 3 print "Fizz" instead of the number
# When the number is divisible by 5 print "Buzz" instead of the number
# When the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number

for number in range(0, 101):
    if (number % 3 == 0) and (number % 5 != 0): # Picks out numbers divisible by 3 but ignores those divisible by 5 also
        print("Fizz")
    elif (number % 5 == 0) and (number % 3 != 0): # Picks out numbers divisible by 5 but ignores those divisible by 3 also
        print("Buzz")
    elif (number % 5 == 0) and (number % 3 == 0): # Picks numbers divisible by BOTH 3 and 5
        print("FizzBuzz")
    else:
        print(number) # Prints the rest of the numbers in the loop
        
# Done
# Textbook solution:

for num in range (1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(number)
    