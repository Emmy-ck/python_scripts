def turn_right():
    turn_left()
    turn_left()
    turn_left()
def stop():
    while at_goal():
        break
def turn():
    while at_goal():
        stop()
    while wall_in_front():
        turn_right()
    while not wall_in_front():
        move()
        if right_is_clear() and not wall_on_right():
            turn_right()
            move()
        while wall_on_right() and front_is_clear():
            move()
            if at_goal():
                stop()
        if wall_on_right() and not front_is_clear():
            turn_left()
            while front_is_clear():
                move()
                if at_goal():
                    stop()
            if not front_is_clear():
                turn_left()
while not at_goal():
    while wall_on_right():
        turn()
        if at_goal():
            stop()
    while not wall_on_right():
        if right_is_clear():
            while at_goal():
                stop
        turn()