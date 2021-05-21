# Draw a dashed line
import turtle as t

my_t = t.Turtle()

for _ in range(20):
    if my_t.isdown():
        my_t.up()
    else:
        my_t.down()

    my_t.forward(10)


screen = t.Screen()
screen.exitonclick()
