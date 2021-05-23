import turtle

SNAKE_MOVEMENT = 20

DEFAULT_COLOR = "white"
DEFAULT_SHAPE = "square"

DIRECTION_UP = 90
DIRECTION_RIGHT = 0
DIRECTION_DOWN = 270
DIRECTION_LEFT = 180


def create_part(color, shape):
    part = turtle.Turtle()
    part.up()
    part.shape(shape)
    part.color(color)
    return part


STARTED_COORDINATE = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self, color=DEFAULT_COLOR, shape=DEFAULT_SHAPE):
        self.parts = []
        for coordinate in STARTED_COORDINATE:
            part = create_part(color, shape)
            part.goto(coordinate)
            self.parts.append(part)

        self.head = self.parts[0]

    def move(self):
        for i in range(len(self.parts)-1, 0, -1):
            next_part = self.parts[i-1]
            self.parts[i].goto(next_part.xcor(), next_part.ycor())

        self.head.forward(SNAKE_MOVEMENT)

    def up(self):
        if self.head.heading() != DIRECTION_DOWN:
            self.head.setheading(DIRECTION_UP)

    def down(self):
        if self.head.heading() != DIRECTION_UP:
            self.head.setheading(DIRECTION_DOWN)

    def left(self):
        if self.head.heading() != DIRECTION_RIGHT:
            self.head.setheading(DIRECTION_LEFT)

    def right(self):
        if self.head.heading() != DIRECTION_LEFT:
            self.head.setheading(DIRECTION_RIGHT)
