import turtle

DEFAULT_MOVE_SPEED = 0.1
MOVE_DISTANCE_X = 10
MOVE_DISTANCE_Y = 10
SPEED_ACCELERATION = 0.9


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.move_x = MOVE_DISTANCE_X
        self.move_y = MOVE_DISTANCE_Y
        self.move_speed = DEFAULT_MOVE_SPEED

        self.shape("circle")
        self.color("white")
        self.up()

    def move(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y

        self.goto(x, y)

    def bounce_x(self):
        """Change ball direction of x coordinate"""
        self.move_x *= -1

    def bounce_y(self):
        """Change ball direction of y coordinate"""
        self.move_y *= -1

    def reset(self):
        """Reset ball position to 0,0 and speed to DEFAULT_MOVE_SPEED"""
        self.home()
        self.move_speed = DEFAULT_MOVE_SPEED

    def increase_speed(self):
        self.move_speed *= SPEED_ACCELERATION


