# You are painting a wall. The instructions on the paint can say that 1 can of paint
# can cover 5 square meters of wall. Given a random height and width of wall,
# calculate how many cans of paint you'll need to buy.
#
#   number of cans = (wall height x wall width) ÷ coverage per can.
#
#   e.g. Height = 2, Width = 4, Coverage = 5
#
# Because you can't buy fractions of a can of paint, the result should be rounded up.
import math


def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil(height * width / cover)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
