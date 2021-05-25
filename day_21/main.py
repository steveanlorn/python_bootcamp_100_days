# Snake food
# Snake eat food
# Score
# Game over state:
# - collide with wall
# - collide with body

import turtle
import snake
import time
import food
import scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

PADDING = 20

BORDER_RIGHT = int(SCREEN_WIDTH/2) - PADDING
BORDER_LEFT = -int(SCREEN_WIDTH/2) + PADDING
BORDER_TOP = int(SCREEN_HEIGHT/2) - PADDING
BORDER_BOTTOM = -int(SCREEN_HEIGHT/2) + PADDING

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

my_snake = snake.Snake()
my_food = food.Food(game_width=SCREEN_WIDTH, game_height=SCREEN_HEIGHT)
my_score_board = scoreboard.ScoreBoard(SCREEN_HEIGHT)
screen.update()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

screen.listen()


while True:
    time.sleep(0.1)
    screen.update()
    my_snake.move()

    if my_snake.head.xcor() > BORDER_RIGHT or my_snake.head.xcor() < BORDER_LEFT or my_snake.head.ycor() > BORDER_TOP or my_snake.head.ycor() < BORDER_BOTTOM:
        my_score_board.game_over()
        break

    if my_snake.is_head_collide_with_body():
        my_score_board.game_over()
        break

    if my_snake.head.distance(my_food.position()) < 15:
        my_score_board.update()
        my_food.spawn()
        my_snake.extend()

screen.exitonclick()
