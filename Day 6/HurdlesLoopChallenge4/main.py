# Complete the "Hurdles Loop Challenge 4" on the Reeborg's World site:
#
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json#
# 
# Solution:
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     move()
#     while not right_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()
#
#
# while at_goal() is False:
#     if wall_in_front():
#         jump()
#     else:
#         move()
