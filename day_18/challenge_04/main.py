# Draw random walk
import turtle as t
import random

my_t = t.Turtle()
my_t.width(7)
my_t.speed(0)

s = t.Screen()
s.colormode(255)

directions = [0, 90, 180, 270]

last_dir = -1

while True:
    direction = random.choice(directions)
    if direction == last_dir:
        continue

    last_dir = direction
    my_t.setheading(direction)

    random_color = (
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
    )
    my_t.color(random_color)

    my_t.forward(20)

s.exitonclick()
