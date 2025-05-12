import time
from turtle import Screen

from mouse import Mouse
from snake import Snake
from scoreboard import Scoreboard


def is_in_range(number, range_start, range_end):
    return range_start <= number <= range_end


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)


scoreboard = Scoreboard()
mouse = Mouse(screen_width=800, screen_height=600)
snake = Snake(screen_width=800, screen_hight=600)

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.listen()

is_game_running = True
while is_game_running:
    screen.update()
    snake.move()
    if is_in_range(snake.head.xcor(), mouse.xcor() - 20, mouse.xcor() + 20) and \
            is_in_range(snake.head.ycor(), mouse.ycor() - 20, mouse.ycor() + 20):
        scoreboard.increase_score()
        mouse.reset_position()
    time.sleep(0.1)

screen.exitonclick()
