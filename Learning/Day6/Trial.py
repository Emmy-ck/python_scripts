def turn_right():
    turn_left()
    turn_left()
    turn_left()
def huddle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

move()
 
# while at_goal != True:
#     while front_is_clear == True:
#         move()
#         if wall_in_front == True:
#             huddle()
#     huddle()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def huddle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        huddle()
    else:
        break