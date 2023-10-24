import json

from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Message(Turtle):
    def __init__(self):
        super().__init__()
        with open('game_settings.json', 'r') as file:
            settings = json.load(file)
        self.screen_width = settings["SCREEN_WIDTH"]
        self.screen_height = settings["SCREEN_HEIGHT"]

        self.color("white")
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(0, self.screen_height/2 - 25)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f" GAME OVER!\n\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_won(self):
        self.home()
        self.write(f" YOU WON!\n\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)
