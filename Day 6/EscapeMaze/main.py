# Complete the "Escape the Maze" challenge on the Reeborg's World site:
#
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json#
#
# Solution:
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

#
# while not at_goal():
#     if not wall_on_right() and front_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front():
#         if not wall_on_right():
#             turn_right()
#             move()
#         else:
#             turn_left()
#     elif wall_on_right() and not wall_in_front():
#         move()
#     else:
#         move()
