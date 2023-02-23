import random
from turtle import Turtle, Screen


def move_forward(turtle, distance):
    turtle.forward(distance)


is_race_on = False
NB_TURTLES = 6
screen = Screen()
screen.setup(height=400, width=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle is gonna win?\n "
                                                           "Enter a color: \n   * red \n   * orange \n   * yellow "
                                                           "\n   * green \n   * blue \n   * purple")

turtles = []
for i in range(0, NB_TURTLES):
    t = Turtle(shape="turtle")
    t.pu()
    t.color(colors[i])
    t.setposition(x=-225, y=(75 - i * 30))
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    moving_turtle = turtles[random.randint(0, NB_TURTLES-1)]
    move_forward(turtle=moving_turtle, distance=random.randint(0, 10))
    if round(moving_turtle.xcor()) >= 225:
        if user_bet == moving_turtle.color()[0]:
            print(f"You win! The {moving_turtle.color()[0]} turtle is the winner.")
        else:
            print(f"You lose... The {moving_turtle.color()[0]} turtle is the winner.")
        break

screen.exitonclick()
