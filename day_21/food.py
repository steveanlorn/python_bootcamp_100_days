import turtle
import random

PADDING = 20


def random_coordinate(game_width, game_height):
    min_x = -int(game_width/2) + PADDING
    max_x = int(game_width/2) - PADDING
    cor_x = random.randint(min_x, max_x)

    min_y = -int(game_height / 2) + PADDING
    max_y = int(game_height / 2) - PADDING
    cor_y = random.randint(min_y, max_y)

    coordinate = (cor_x, cor_y)
    return coordinate


class Food(turtle.Turtle):
    def __init__(self, game_width, game_height):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.up()

        self.game_width = game_width
        self.game_height = game_height

        self.spawn()

    def spawn(self):
        coordinate = random_coordinate(self.game_width, self.game_height)
        self.goto(coordinate)
