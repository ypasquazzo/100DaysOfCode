from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.pu()
        self.setposition(0, 280)
        self.hideturtle()
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Current score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_scoreboard()
