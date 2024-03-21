def turn_right():
    turn_left()
    turn_left()
    turn_left()
def huddle():
    turn_left()
    if not front_is_clear():
        turn_left()
    move()
    while wall_on_right():
        if not front_is_clear():
            turn_left()
        move()
    else:
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
while not at_goal():
    if wall_in_front():
        huddle()
    else:
        move()
while at_goal():
    break