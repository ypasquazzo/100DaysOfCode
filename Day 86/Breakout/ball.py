import json
import random

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        with open('game_settings.json', 'r') as file:
            settings = json.load(file)
        self.ball_speed = settings["BALL_SPEED"]
        self.ball_size = settings["BALL_RADIUS"]

        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=self.ball_size/20)
        self.pu()
        self.dx = 0.01 * random.randint(10, 45)
        self.dy = -0.01 * self.ball_speed

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
