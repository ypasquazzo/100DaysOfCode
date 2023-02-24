from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        x = x - x % 20
        y = y - y % 20
        self.setposition(x, y)
