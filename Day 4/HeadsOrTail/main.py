# You are going to write a virtual coin toss program.
# It will randomly tell the user "Heads" or "Tails".
import random

if random.randint(0, 1) == 1:
    print("Heads")
else:
    print("Tails")
