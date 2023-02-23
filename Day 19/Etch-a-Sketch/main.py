from turtle import Turtle, Screen


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def rotate_clockwise():
    t.setheading(t.heading() - 10)


def rotate_anticlockwise():
    t.setheading(t.heading() + 10)


def clear_screen():
    t.pu()
    t.setposition(0, 0)
    t.pd()
    t.clear()


t = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=rotate_anticlockwise)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()
