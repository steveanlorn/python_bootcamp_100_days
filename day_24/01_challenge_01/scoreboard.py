import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self, game_height):
        super().__init__()
        self.score = 0

        self.high_score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.ht()
        self.up()
        self.setposition(0, int(game_height/2) - 30)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        self.score = 0
        self.write_score()

    def update(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

        self.write_score()
