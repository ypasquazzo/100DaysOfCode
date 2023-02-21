# Number Guessing Game Objectives:
#
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.s
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random

chances = 5

print(art.logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff == "easy":
    chances = 10

while chances > 0:

    if chances == 1:
        print("This is your last attempt, make it count:")
    else:
        print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if num > guess:
        print("Too low.")
    elif num < guess:
        print("Too high.")
    else:
        print(f"You got it! The answer was {num}.")
        break
    chances -= 1
    print("Guess again.")

if chances == 0:
    print(f"You lose! The answer was {num}.")
