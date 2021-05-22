import turtle
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

FINISH_LINE = int(SCREEN_WIDTH/2) - 30

s = turtle.Screen()
s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

colors = ("red", "green", "blue", "orange", "grey", "purple")

turtles = []
for i in range(len(colors)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])

    t.up()
    t.setheading(180)
    t.forward(230)
    t.setheading(0)

    t.goto(-230, -85 + (i * 30))
    turtles.append(t)

# finish line
line = turtle.Turtle()
line.width(3)
line.up()
line.goto(FINISH_LINE, int(SCREEN_HEIGHT/2))
line.setheading(270)
line.down()
line.forward(SCREEN_HEIGHT)

list_color = ', '.join(colors)
user_bet = s.textinput("Place Your Bet", f"Choose color: {list_color}")

winner = None
while winner is None:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() >= FINISH_LINE:
            winner = t
            break

if user_bet.lower() == winner.pencolor():
    print("You win")
else:
    print("You lose")

print(f"winner is {winner.pencolor()}")

s.exitonclick()
