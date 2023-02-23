from turtle import Turtle

STEP = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT: int = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.initialise()

    def initialise(self):
        for i in range(0, 3):
            t = Turtle(shape="square")
            t.pu()
            t.color("white")
            t.setx(i * -STEP)
            self.segments.append(t)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setposition(self.segments[i - 1].pos())
        self.segments[0].fd(STEP)

    def go_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def go_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def go_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def go_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
