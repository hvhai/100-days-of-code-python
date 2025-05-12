
import random
from turtle import Turtle


class Mouse:
    def __init__(self, screen_width, screen_height):
        self.mouse = Turtle()
        self.mouse.penup()
        self.mouse.shape("square")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()

    def reset_position(self):
        self.mouse.goto(random.randint(-self.screen_width // 2 + 20, self.screen_width // 2 - 20),
                        random.randint(-self.screen_height // 2 + 20, self.screen_height // 2 - 20))

    def xcor(self):
        return self.mouse.xcor()

    def ycor(self):
        return self.mouse.ycor()
