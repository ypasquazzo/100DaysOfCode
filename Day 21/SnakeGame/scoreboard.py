from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.pu()
        self.setposition(0, 280)
        self.hideturtle()
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Current score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
