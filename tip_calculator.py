#The program should look like this:
#Welcome to the tip calculator.
#What was the total bill? $124.56
#What percentage tip would you like to give? 10, 12, or 15? 12
#How many people are splitting the bill? 7
#Each person should pay: $19.93
#------------------------------------------------------------------------------------#
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people are splitting the bill? "))
#------------------------------------------------------------------------------------#
percent_tip = round(tip / 100, 2) #rounds off the tip percetage to 2 decimal points and assigns to variable percentage tip
amount = round(((1 + percent_tip) * bill) / people, 2) #simplified formular of the calculations

print(f"Each person should pay: ${amount}")

#Done

#Here are a few ways we can format floating point numbers:
#a = 13.765932108275950
#print(a)
#13.765
#print("%.2f" % a)
#13.77
#round(a,2)
#13.77
#print("%.2f" % round(a, 2))
#13.77
#print("{:.2f}".format(a))
#13.77
#print("{:.2f}".format(round(a, 2)))
#13.77
#print("{.15f}".format(round(a, 2)))
#13.765932108275950