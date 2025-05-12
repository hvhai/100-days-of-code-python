from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.display = Turtle()
        self.display.penup()
        self.display.goto(0, 250)
        self.display.hideturtle()
        self.update_score()

    def update_score(self):
        self.display.clear()
        self.display.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
