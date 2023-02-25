from turtle import Turtle

STEP = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT: int = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.positions = [(0, 0), (-STEP, 0), (2 * -STEP, 0)]
        self.initialise()
        self.head = self.segments[0]

    def initialise(self):
        for position in self.positions:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.pu()
        t.color("white")
        t.setposition(position)
        self.segments.append(t)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.initialise()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setposition(self.segments[i - 1].pos())
        self.head.fd(STEP)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
