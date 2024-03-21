#Don't change the code below
#-------------------------------------------------------------#
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
#-------------------------------------------------------------#
#Write a program that calculates the Body Mass Index(BMI)
# from a user's weight and height
#BMI =weight(kgs) / height^2(m^2)

a = float(weight)
b = float(height) * float(height)

bmi = a/b
c = int(bmi)

print("Your BMI is " + str(c))

#Done
#Another solution:
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_to_int = int(bmi)

print(bmi_to_int)
