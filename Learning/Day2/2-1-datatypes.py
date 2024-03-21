#Don't change the code below:
#--------------------------------------------------------------------------#
two_digit_number = input("Type a two digit number: ")
#--------------------------------------------------------------------------#
#Result should be the sum of the first number and the second number
# in the 2-digit number entered by the user
#Code should work with ay given number

a = int(two_digit_number[0])
b = int(two_digit_number[1])

print(a + b)

#Done
#Another way of doing it:
two_digit_number = input("Type a two digit number: ")

a = two_digit_number[0]
b = two_digit_number[1]

result = int(a) + int(b)
print(result)