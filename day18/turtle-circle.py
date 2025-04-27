from turtle import Turtle
import random

t = Turtle()
t.screen.colormode(255)

t.speed("fastest")
size_of_gap = 10
for i in range(int(360 / size_of_gap)):
    t.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.circle(100)
    t.setheading(t.heading() + size_of_gap)
    # t.left(i * 2)

t.screen.mainloop()
