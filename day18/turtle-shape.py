import random
from turtle import Turtle

shape_turle = Turtle()

shape_turle.screen.colormode(255)

for path_number in range(3, 12):
    shape_turle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    for _ in range(path_number):
        shape_turle.forward(100)
        shape_turle.left(360 / path_number)

shape_turle.screen.mainloop()
