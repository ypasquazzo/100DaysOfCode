from turtle import Turtle
import random

BALL_SPEED = 0.2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=0.75)
        self.setheading(random.randint(20, 50))
        self.pace = BALL_SPEED

    def move(self):
        self.fd(self.pace)

    def bounce_wall(self):
        self.setheading(-self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.pace *= 1.02
