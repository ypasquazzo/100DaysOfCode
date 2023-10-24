import json

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        with open('game_settings.json', 'r') as file:
            settings = json.load(file)
        self.screen_width = settings["SCREEN_WIDTH"]
        self.paddle_speed = settings["PADDLE_SPEED"]
        self.paddle_height = settings["PADDLE_HEIGHT"]
        self.paddle_width = settings["PADDLE_WIDTH"]

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.paddle_height/20, stretch_len=self.paddle_width/20)
        self.pu()
        self.goto(0, x)

    def move_left(self):
        if self.xcor() > -(self.screen_width/2 - self.paddle_width/2):
            self.bk(self.paddle_speed)

    def move_right(self):
        if self.xcor() < self.screen_width/2 - self.paddle_width/2:
            self.fd(self.paddle_speed)
