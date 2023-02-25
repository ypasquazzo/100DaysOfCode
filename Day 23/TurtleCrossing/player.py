from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 230
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setposition(STARTING_POSITION)
        self.setheading(UP)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def check_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        self.setposition(STARTING_POSITION)
