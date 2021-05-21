# damien hirst dot painting
import random
import turtle as t
import colorgram

colors = colorgram.extract("damien-hirst-paintings-spot-painting.jpeg", 35)

t.setworldcoordinates(-1, -1, 20, 20)

my_t = t.Turtle(visible=False)
my_t.up()
my_t.speed(0)

s = t.Screen()
s.colormode(255)
print(s.canvwidth)
print(s.canvheight)

for y in range(20):
    for x in range(20):
        print(f"{my_t.pos()}", x)
        random_color = random.choice(colors)
        my_t.goto(x, y)
        my_t.dot(20, (random_color.rgb.r, random_color.rgb.g, random_color.rgb.b))



s.exitonclick()
