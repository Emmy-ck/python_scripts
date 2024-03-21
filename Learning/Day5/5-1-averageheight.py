# Write a program that calculates the average student height from a list of heights.
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# Average heights is rounded off to the nearest whole number.
# Don't change the code below: 
# You are not allowed to use the len() fuction or the sum() function
#------------------------------------------------------------------------------------------------------------------------------#
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
#------------------------------------------------------------------------------------------------------------------------------#

# minimum_range = int(student_heights.index(student_heights[0])) #converts the first item to it's index 0 on the list. This determines the minimum of the range
maximum_range = int(student_heights.index(student_heights[-1]))

# print(minimum_range)
total_students = (maximum_range + 1)
total_sum = 0

for i in student_heights:
    total_sum += i

average_height = round(total_sum / total_students) # Do not add any argument in round to make it a whole number

print(f'The average height of {total_students} is {average_height}')

#Done
#Here is a better way of doing it:
#The code not to be changed below:
#-------------------------------------------------------------------------
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
#-------------------------------------------------------------------------

total_height = 0 #Create a variable to track the total height, set the initial value to 0
# The loop belew is an equivalent of the sum() function
for height in student_heights: # Take individual items inside the list
    total_height += height # Add each item to total_sum 0 to keep accumulating
print(total_height) # Print total outside the for loop to print the final result only

number_of_students = 0 # Create a variable to track the total number of students in the list, set initial to 0
# The loop below is an equivalent of the len() function
for students in student_heights:
    number_of_students += 1 # Find the total number of items in the list of student heights
print(number_of_students)

average_height1 = round(total_height / number_of_students)

print(average_height1)