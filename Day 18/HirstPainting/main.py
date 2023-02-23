# Code to generate the initial colour_list only needs to run once.
# import colorgram
#
# rgb_colors_raw = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors_raw.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors_raw)

from turtle import Turtle, Screen
import random


def draw_circle():
    t.fillcolor(random.choice(colour_list))
    t.pd()
    t.begin_fill()
    t.circle(circle_rad)
    t.end_fill()
    t.pu()


t = Turtle()
screen = Screen()
screen.colormode(255)
colour_list = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88),
               (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84),
               (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241),
               (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107),
               (222, 177, 169), (181, 188, 208), (171, 203, 193)]
circle_rad = 5
space = 25
bump = 2 * circle_rad + space
t.pu()
t.speed("fastest")
t.ht()

for i in range(0, 10):
    t.setpos(-162.5, -162.5 + i * bump)
    for _ in range(0, 10):
        draw_circle()
        t.fd(bump)

t.setpos(0, 0)
screen.exitonclick()
