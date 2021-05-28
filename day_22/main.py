import turtle
import scoreboard
import players
import balls
import time

GAME_SCREEN_WIDTH = 800
GAME_SCREEN_HEIGHT = 600

game_screen = turtle.Screen()
game_screen.setup(width=GAME_SCREEN_WIDTH, height=GAME_SCREEN_HEIGHT)
game_screen.bgcolor("black")
game_screen.title("PONG")
game_screen.tracer(0)

divider = turtle.Turtle()
divider.up()
divider.goto(0, int(GAME_SCREEN_HEIGHT / 2))
divider.down()
divider.ht()
divider.color("grey")
divider.width(3)
divider.setheading(270)
for i in range(1, GAME_SCREEN_HEIGHT, 10):
    if divider.isdown():
        divider.up()
    else:
        divider.down()

    divider.forward(10)

left_score = scoreboard.Scoreboard((-40, int(GAME_SCREEN_HEIGHT/2) - 60))
right_score = scoreboard.Scoreboard((40, int(GAME_SCREEN_HEIGHT/2) - 60))

left_player = players.Player((-int(GAME_SCREEN_WIDTH/2) + 50, 0))
right_player = players.Player((int(GAME_SCREEN_WIDTH/2) - 50, 0))

max_score = int(game_screen.textinput("SCORE TO WIN", "Put maximum score to win the game: "))

game_screen.onkey(left_player.move_up, "w")
game_screen.onkey(left_player.move_down, "s")
game_screen.onkey(right_player.move_up, "Up")
game_screen.onkey(right_player.move_down, "Down")
game_screen.listen()

game_ball = balls.Ball()

game_screen.update()

is_game_restart = False

while True:
    if game_ball.ycor() >= 290 or game_ball.ycor() <= - 290:
        """When ball hit upper and lower wall"""
        game_ball.bounce_y()

    if game_ball.distance(right_player) < 50 and game_ball.xcor() > 320 or game_ball.distance(left_player) < 50 and game_ball.xcor() < -320:
        """When ball hit player's paddle"""
        game_ball.bounce_x()
        game_ball.increase_speed()

    if game_ball.xcor() > int(GAME_SCREEN_WIDTH/2):
        """When right player failed to bounce the ball"""
        left_score.score += 1
        left_score.write_score()
        is_game_restart = True

    if game_ball.xcor() < -int(GAME_SCREEN_WIDTH/2):
        """When left player failed to bounce the ball"""
        right_score.score += 1
        right_score.write_score()
        is_game_restart = True

    if is_game_restart:
        if left_score.score >= max_score or right_score.score >= max_score:
            break

        is_game_restart = False
        game_ball.bounce_x()
        game_ball.reset()
        time.sleep(1)
        continue

    game_ball.move()
    game_screen.update()
    time.sleep(game_ball.move_speed)

winner_player = "left"
if right_score.score == max_score:
    winner_player = "right"

winner = turtle.Turtle()
winner.color("white")
winner.ht()
winner.up()
winner.write(f"{winner_player.upper()} WIN!", align="center", font=("Courier", 45, "normal"))

game_screen.exitonclick()
