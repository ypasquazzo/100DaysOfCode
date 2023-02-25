from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 0
        self.pu()
        self.hideturtle()
        self.setposition(-380, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"PLAYER SCORE: {self.score}", align=ALIGNMENT, font=FONT)
