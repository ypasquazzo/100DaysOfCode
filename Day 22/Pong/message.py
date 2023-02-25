from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.pu()
        self.hideturtle()

    def game_over(self, winner):
        self.home()
        self.write(f"  GAME OVER!\n\n{winner} player wins.", align=ALIGNMENT, font=FONT)
