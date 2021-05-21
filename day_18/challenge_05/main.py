# Draw a spirograph

import turtle as t
import random

my_t = t.Turtle()
s = t.Screen()
s.colormode(255)

my_t.speed(0)
my_t.width(2)

for _ in range(int(360/5)):
    random_color = (
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
    )
    my_t.color(random_color)
    my_t.circle(100)
    my_t.left(5)

s.exitonclick()
