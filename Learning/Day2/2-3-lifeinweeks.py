#Create a program using math and f-strings that tells us 
#how many days, weeks months we have left if we live until 90 years.
#Take your current age as input and output a message with our time left in this format:
#You have x days, y weeks and z months left.
#Do not change the code below:
#-------------------------------------------------------------------#
#This first program I created does a countdown
age = input("What is your current age? ")
year = 90
#-------------------------------------------------------------------#
age = int(age)
year = int(year)

k = (year - age)
days = (k * 365)

months = (days // 30)
z = int(months)

remdays1 = (days - (z * 30))
weeks = (remdays1 // 7)
y = int(weeks)

remdays2 = (remdays1 - (y * 7))
x = int(remdays2)

print(f"You have {x} days, {y} weeks and {z} months left")

#Done
#In this second method, it accounts for total days, total weeks and total months
#simultaneously. Meaning days are counted in days, weeks and months,
#weeks are counted in weeks and months and months in months

age = input("What is your current age? ")
age = int(age)
year = 90

k = (year - age)
k = int(k)

days = (k * 365)
weeks = (k * 52)
months = (k * 12)

print(f"You have {days} days, {weeks} weeks and {months} months remaining")