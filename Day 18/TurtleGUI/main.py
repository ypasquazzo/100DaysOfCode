# Exercises around the Turtle GUI module
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()
colours = ["CornflowerBlue", "DarkOrchid",
           "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]


# 1. Draw a square
# for i in range(4):
#     my_turtle.rt(90)
#     my_turtle.fd(100)

# 2. Draw a dotted line
# for i in range(20):
#     my_turtle.fd(5)
#     my_turtle.pu()
#     my_turtle.fd(5)
#     my_turtle.pd()

# 3. Draw 5 shapes imbricated
# for i in range(5):
#     my_turtle.color(random.choice(colours))
#     for j in range(i+3):
#         my_turtle.rt(360/(i+3))
#         my_turtle.fd(100)

# 4. Draw a random line
# angles = [0, 90, 180, 270]
# my_turtle.pensize(10)
# my_turtle.speed("fast")
# for i in range(100):
#     my_turtle.color(random.choice(colours))
#     my_turtle.rt(random.choice(angles))
#     my_turtle.fd(50)

# 5. Same as #4 but with random color line
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     t = (r, g, b)
#     return t
#
#
# angles = [0, 90, 180, 270]
# screen.colormode(255)
# my_turtle.pensize(10)
# my_turtle.speed("fast")
# for i in range(100):
#     my_turtle.color(random_color())
#     my_turtle.rt(random.choice(angles))
#     my_turtle.fd(50)

# 6. Draw a random color Spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t = (r, g, b)
    return t


screen.colormode(255)
my_turtle.speed("fastest")
heading = 0
num_drawings = 100
for i in range(0, num_drawings):
    my_turtle.setheading(heading)
    my_turtle.color(random_color())
    my_turtle.circle(100)
    heading += 360 / num_drawings

screen.exitonclick()
