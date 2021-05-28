import turtle


class Scoreboard (turtle.Turtle):
    def __init__(self, position):
        super().__init__()

        self.score = 0

        self.color("grey")
        self.up()
        self.ht()
        self.goto(position)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(self.score, align="center", font=("Courier", 45, "normal"))
