#Don't change the code below:
n = int(input("Check this number: "))
def prime_checker(number=n):
    is_prime = True
    for num in range(2, number):
        if (number % num == 0):
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")
prime_checker(number=n)

# Done
# another solution