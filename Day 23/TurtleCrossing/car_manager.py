from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
LEFT = 180


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.segments = []
        self.color = COLORS[random.randint(0, len(COLORS)-1)]
        self.pace = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level
        self.y = (random.randint(-200, 220))
        self.positions = [(380, self.y), (370, self.y)]
        self.initialise()

    def initialise(self):
        for position in self.positions:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.pu()
        t.color(self.color)
        t.setheading(LEFT)
        t.setposition(position)
        self.segments.append(t)

    def move(self):
        self.segments[0].fd(self.pace)
        self.segments[1].fd(self.pace)

    def increase_speed(self):
        self.pace += MOVE_INCREMENT
