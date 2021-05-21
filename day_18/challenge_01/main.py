# Draw a square

import turtle as t

my_t = t.Turtle()

for _ in range(4):
    my_t.forward(100)
    my_t.right(90)

s = t.Screen()
s.exitonclick()
