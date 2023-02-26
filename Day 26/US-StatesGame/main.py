import turtle
from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


def display_state(name, x, y):
    t = Turtle()
    t.color("black")
    t.pu()
    t.hideturtle()
    t.setposition(x, y)
    t.write(f"{name}", align=ALIGNMENT, font=FONT)


def record_missing_list():
    missing_states = [s for s in states if s not in correct_guess]
    df = pandas.DataFrame(missing_states, columns=["State"])
    df.to_csv("missing_states.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
correct_guess = []

while len(correct_guess) < 50:

    answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state name? ")
    answer = answer.title()

    if answer == "Exit":
        record_missing_list()
        break

    for state in states:
        if answer == state:
            row = data[data.state == answer]
            display_state(answer, int(row.x), int(row.y))
            correct_guess.append(answer)

    display_state("YOU FOUND ALL 50 STATES!", 0, 270)

screen.exitonclick()
