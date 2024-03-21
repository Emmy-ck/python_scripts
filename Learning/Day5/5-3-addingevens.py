# Write a program that calculates the sum of all even numbers from 1 to 100.
# There should only be 1 print statement in our console output
# It should only print the final total and not every step of the calculation

total = 0
for number in range(0, 101, 2):
    total += number
print(total)

# Done
# Another way of doing it, my way
summ = 0
for n in range(1, 101):
    if n % 2 == 0:
        summ += n
print(summ)