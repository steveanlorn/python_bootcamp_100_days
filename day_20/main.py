# 1. Snake body
# 2. Snake movement
# 3. Snake controller

import turtle
import snake
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

my_snake = snake.Snake()
screen.update()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

screen.listen()

while True:
    time.sleep(0.2)
    screen.update()
    my_snake.move()
