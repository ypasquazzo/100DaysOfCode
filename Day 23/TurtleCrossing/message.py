from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.pu()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
