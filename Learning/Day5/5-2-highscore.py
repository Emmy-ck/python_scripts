# Write a program that calculates the highest score from a list of scores
# You are not allowed to use the max or min functions.
# The output words must be : 'The highest score in the class is: x'
# Do not change the code below:
#-----------------------------------------------------------------------------
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
#-----------------------------------------------------------------------------
# The for loop below does the same thing as the max function

for i in range(0, len(student_scores)): # Pick the individual items in the list by their index
    high_score = student_scores[i] # Assign the number at index i to the high score variable
    for score in student_scores: # Pick the individual scores in the list and iterates through them
        if score > high_score: # Compares the scores with the value at index i of the list which has been assigned the variable name 'high_score'
            high_score = score

print(f'The highest score in the class is {high_score}')

# Done
# Here's another solution:

highest_score = 0
for score1 in student_scores:
    if score1 > highest_score:
        highest_score = score1
print(f"The highest score is {highest_score}")