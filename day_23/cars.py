import turtle
import random

COLORS = ("red", "green", "blue", "grey", "orange", "purple", "pink", "aqua")


class Car(turtle.Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.up()
        self.goto(position)

    def move(self, speed):
        self.forward(speed)
