# create an etch-a-sketch app
# w to move forward
# s to move backward
# a to go counter-clockwise
# d to go clockwise
# c to clear the screen

import turtle

t = turtle.Turtle()
s = turtle.Screen()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def counter_clockwise():
    t.left(10)


def clockwise():
    t.right(10)


def clear():
    t.clear()


s.onkey(forward, "w")
s.onkey(backward, "s")
s.onkey(counter_clockwise, "a")
s.onkey(clockwise, "d")
s.onkey(clear, "c")

s.listen()
s.exitonclick()
