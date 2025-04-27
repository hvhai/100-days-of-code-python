import random
from turtle import Turtle
import colorgram

colors = colorgram.extract("day18/color-palettes.png", 36)

rgb_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

t = Turtle()
t.screen.colormode(255)
number_of_dot = 10

t.penup()
t.goto(-200, -200)
for y in range(number_of_dot):
    for x in range(number_of_dot):
        t.dot(20, random.choice(rgb_list))
        t.forward(50)
    if y % 2 == 0:
        t.dot(20, random.choice(rgb_list))
        t.left(90)
        t.forward(50)
        t.left(90)
    else:
        t.dot(20, random.choice(rgb_list))
        t.right(90)
        t.forward(50)
        t.right(90)


t.screen.mainloop()
