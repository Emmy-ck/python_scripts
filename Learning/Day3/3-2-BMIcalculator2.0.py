#Write a program that interprets the BMI based on a user's weight and height
#The interpretation should be:
#   Under 18.5 = Underweight
#   Over 18.5 but below 25 = Normal weight
#   Over 25 but below 30 = Overweight
#   Over 30 but below 35 = Obese
#   Above 35 = Clinically obese
#Do not change the code below:
#-------------------------------------------------------#
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
#-------------------------------------------------------#
bmi = (weight / (height ** 2))
bmi = round(bmi, 1) #Convert BMI to float with 1 decimal point

if bmi < 18.5:
    print(f"BMI = {bmi} - Underweight")
elif bmi > 18.5 and bmi <= 25:
    print(f"BMI = {bmi} - Normal Weight")
elif bmi > 25 and bmi <= 30:
    print(f"BMI = {bmi} - Overweight")
elif bmi > 30 and bmi <= 35:
    print(f"BMI = {bmi} - Obese")
else:
    print(f"BMI = {bmi} - Clinically Obese")
    
#Done
#Another solution is:

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height ** 2), 1)

if bmi <= 18.5:
    print(f"BMI = {bmi} - Underweight")
elif bmi <= 25:
    print(f"BMI = {bmi} - Normal Weight")
elif bmi <= 30:
    print(f"BMI = {bmi} - Overweight")
elif bmi <= 35:
    print(f"BMI = {bmi} - Obese")
else:
    print(f"BMI = {bmi} - Clinically Obese")