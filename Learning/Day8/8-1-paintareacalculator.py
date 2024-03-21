# 1 can of paint can paint 5 square meters
# Given a random height and width pf the wall
# Calculate how many cans of paint needed to buy

#number of cans = (wall height x wall width) / covverage per can
# Because you can't buy half cans, round up to nearest whole number
# Result: You'll need x cans of paint
# Write your code abebve here:
import math
test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
def paint_calc(height=test_h, width=test_w,cover=coverage) :
    cans = math.ceil((height * width ) / cover) # Rounding up to the nearest whole number
    print(f"You will need {cans} cans of paint")
# Don't change the code below:
#--------------  ------------------------------------------------------------#
paint_calc(height=test_h, width=test_w, cover=coverage)
#--------------------------------------------------------------------------#

# Done
# Another solution: