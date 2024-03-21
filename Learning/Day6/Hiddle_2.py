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

move()
 
while at_goal != True:
    while front_is_clear == True:
        move()
        if wall_in_front == True:
            huddle()
    huddle()