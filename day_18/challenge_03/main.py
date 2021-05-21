# Draw shapes:
# - triangle
# - square
# - pentagon
# - hexagon
# - heptagon
# - octagon
# - nonagon
# - decagon

import turtle as t
import random

my_t = t.Turtle()

colors = ["red", "blue", "yellow", "brown", "purple", "green", "black", "gray", "gold"]


def draw_shape(length, side):
    for _ in range(side):
        my_t.right(360/side)
        my_t.forward(length)


for side in range(3, 11):
    color = random.choice(colors)
    my_t.color(color)
    draw_shape(100, side)

screen = t.Screen()
screen.exitonclick()
my_t = t.Turtle()
