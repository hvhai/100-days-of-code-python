import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

position_segment = [(-40, 0), (-20, 0), (0, 0)]
turtle_segment = []
for segment in position_segment:
    turtle = Turtle()
    turtle.penup()
    turtle.speed(1)
    turtle.shape("square")
    turtle.goto(segment)
    turtle_segment.append(turtle)


def calculate_x(x):
    return x + 20 if x < 400 else -400


def calculate_next_position(x, y):
    return (calculate_x(x), y)


is_game_running = True
while is_game_running:
    screen.update()
    x, y = position_segment[2]
    next_position = calculate_next_position(x, y)
    new_possition_segment = [position_segment[1], position_segment[2], next_position]

    for turtle, position in zip(turtle_segment, new_possition_segment):
        turtle.goto(position)
    position_segment = new_possition_segment
    time.sleep(0.5)

screen.exitonclick()
