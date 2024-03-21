def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while wall_in_front():
        turn_right()
    while not wall_in_front():
        move()
        while wall_on_right() and front_is_clear():
            move()
        if wall_on_right() and not front_is_clear():
            turn_left()
            while front_is_clear():
                move()
            if not front_is_clear():
                turn_left()
while at_goal():
    break