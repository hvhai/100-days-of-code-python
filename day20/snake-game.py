import time
from turtle import Turtle, Screen, width

MOVE_DISTANCE = 20


class Snake:
    def __init__(self, screen_width, screen_hight):
        self.max_x = screen_width / 2
        self.max_y = screen_hight / 2
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[2]

    def create_snake(self):
        for segment in [(-40, 0), (-20, 0), (0, 0)]:
            turtle = Turtle()
            turtle.penup()
            turtle.speed(1)
            turtle.shape("square")
            turtle.goto(segment)
            self.snake_segments.append(turtle)

    def move(self):
        new_x = self.snake_segments[1].xcor()
        new_y = self.snake_segments[1].ycor()
        self.snake_segments[0].goto(new_x, new_y)

        new_x = self.snake_segments[2].xcor()
        new_y = self.snake_segments[2].ycor()
        self.snake_segments[1].goto(new_x, new_y)

        head_x = self.head.xcor()
        head_y = self.head.ycor()
        match self.head.heading():
            case 0 if self.head.xcor() > self.max_x - 10:
                self.head.goto(-self.max_x, head_y)
            case 90 if self.head.ycor() > self.max_y - 10:
                self.head.goto(head_x, -self.max_y)
            case 180 if self.head.xcor() < -self.max_x + 10:
                self.head.goto(self.max_x, head_y)
            case 270 if self.head.ycor() < -self.max_y + 10:
                self.head.goto(head_x, self.max_y)
            case _:
                self.head.forward(MOVE_DISTANCE)


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

snake = Snake(screen_width=800, screen_hight=600)


def calculate_x(x):
    return x + 20 if x < 400 else -400


def calculate_next_position(x, y):
    return (calculate_x(x), y)


is_game_running = True
while is_game_running:
    screen.update()
    snake.move()
    time.sleep(0.5)

screen.exitonclick()
