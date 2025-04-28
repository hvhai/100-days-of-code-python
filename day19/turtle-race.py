import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtle_list = []
for index, color in enumerate(rainbow_colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, index * 30)
    turtle_list.append(new_turtle)
user_bet = screen.textinput("Race", "Predict winner? Enter a color")


def run():
    is_the_race_on = True

    while is_the_race_on:
        for turtle in turtle_list:
            turtle.forward(random.randint(10, 30))
            if turtle.xcor() > 230:
                is_the_race_on = False
                if turtle.pencolor() == user_bet:
                    print("You are winner!")
                else:
                    print(f"You're lost! The winner is {turtle.pencolor()}")


screen.onkey(key="a", fun=run)

screen.listen()
screen.exitonclick()
