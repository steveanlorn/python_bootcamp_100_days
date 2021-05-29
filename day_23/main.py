import turtle
import players
import car_manager
import level_manager
import time

GAME_SCREEN_WIDTH = 600
GAME_SCREEN_HEIGHT = 600

PADDING = 20
MARGIN_TOP = int(GAME_SCREEN_HEIGHT/2) - PADDING
MARGIN_BOTTOM = -int(GAME_SCREEN_HEIGHT/2) + PADDING
MARIN_LEFT = -int(GAME_SCREEN_WIDTH/2) + PADDING
MARGIN_RIGHT = int(GAME_SCREEN_WIDTH / 2) + PADDING

FINISH_LINE = MARGIN_TOP

game_screen = turtle.Screen()
game_screen.setup(width=GAME_SCREEN_WIDTH, height=GAME_SCREEN_HEIGHT)
game_screen.title("Cross The Road Game")
game_screen.bgcolor("black")
game_screen.tracer(0)

player = players.Player((0, MARGIN_BOTTOM))

game_screen.onkey(player.move, "Up")
game_screen.listen()

MAX_CAR_LINE = MARGIN_TOP - 20
MIN_CAR_LINE = MARGIN_BOTTOM + 20
my_car_manager = car_manager.CarManager(MARGIN_RIGHT, MIN_CAR_LINE, MAX_CAR_LINE, 20)

my_level_manager = level_manager.LevelManager((MARIN_LEFT, MARGIN_TOP - 20))

while True:
    if player.ycor() == FINISH_LINE:
        player.go_to_start()
        my_level_manager.increase_level()
        my_level_manager.write_level()

    my_car_manager.deploy_car()
    my_car_manager.move_cars(my_level_manager.speed)

    if my_car_manager.is_hit_player(player):
        break

    game_screen.update()
    time.sleep(0.1)

game_over = turtle.Turtle()
game_over.color("white")
game_over.up()
game_over.ht()
game_over.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
game_screen.exitonclick()
