import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self, game_height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.up()
        self.setposition(0, int(game_height/2) - 30)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def update(self):
        self.score += 1
        self.write_score()
