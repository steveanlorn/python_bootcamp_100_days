import turtle

MOVE_SPEED = 20
PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1


class Player(turtle.Turtle):
    def __init__(self, position):
        super().__init__()

        self.move_speed = MOVE_SPEED

        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.up()
        self.setheading(90)
        self.goto(position)

    def move_up(self):
        self.forward(self.move_speed)

    def move_down(self):
        self.backward(self.move_speed)
