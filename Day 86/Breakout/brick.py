import json

from turtle import Turtle


class Brick(Turtle):
    def __init__(self, col: float, row: float, color: str):
        super().__init__()
        with open('game_settings.json', 'r') as file:
            settings = json.load(file)
        self.screen_width = settings["SCREEN_WIDTH"]
        self.screen_height = settings["SCREEN_HEIGHT"]
        self.brick_height = settings["BRICK_HEIGHT"]
        self.brick_width = settings["BRICK_WIDTH"]

        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=self.brick_height/20, stretch_len=self.brick_width/20)
        self.pu()
        x = -self.screen_width / 2 + col * (self.brick_width + 5) + self.brick_width/2
        y = self.screen_height / 2 - row * (self.brick_height + 10) - self.brick_height / 2 - 25
        self.goto(x, y)
