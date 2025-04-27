from turtle import Turtle
import random

walker = Turtle()
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

walker.pensize(5)
walker.speed(10)
for _ in range(200):
    walker.color(random.choice(rainbow_colors))  # Set a random rainbow color
    walker.forward(30)
    walker.left(random.choice([0, 90, 180, 270]))


walker.screen.mainloop()
