from turtle import Turtle

UP = 90
DOWN = 270
PADDLE_SPEED = 35


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.setx(x)

    def move_up(self):
        self.fd(PADDLE_SPEED)

    def move_down(self):
        self.bk(PADDLE_SPEED)
