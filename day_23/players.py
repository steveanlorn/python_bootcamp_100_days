import turtle


class Player (turtle.Turtle):
    def __init__(self, position):
        super().__init__()

        self.starting_position = position

        self.shape("turtle")
        self.color("white")
        self.up()
        self.setheading(90)
        self.goto(position)

    def move(self):
        self.forward(20)

    def go_to_start(self):
        self.goto(self.starting_position)
