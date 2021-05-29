import turtle

SPEED_INCREMENT = 2
FONT = ("Courier", 26, "normal")
ALIGNMENT = "left"


class LevelManager(turtle.Turtle):
    def __init__(self, position):
        super().__init__()

        self.level = 1
        self.speed = 5

        self.color("white")
        self.ht()
        self.up()
        self.goto(position)
        self.write_level()

    def increase_level(self):
        self.level += 1
        self.speed += SPEED_INCREMENT

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
