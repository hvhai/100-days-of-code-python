from turtle import Turtle

turtle = Turtle()

turtle.speed(1)
for _ in range(5):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

turtle.screen.title("My square")
turtle.screen.mainloop()
