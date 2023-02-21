# Build a game of 'Higher/Lower' as showcased here:
# https://replit.com/@appbrewery/higher-lower-final?v=1#game_data.py

import art
import game_data
import os
import random

print(art.logo)
score = 0
data = game_data.data
size = len(game_data.data)

a = random.randint(0, size-1)
b = random.randint(0, size-1)
while a == b:
    b = random.randint(0, size - 1)

while True:
    follower = data[a]['follower_count']

    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}.")
    print(art.vs)
    print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")

    os.system('cls')

    if data[b]['follower_count'] > follower:
        if choice == "A":
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        else:
            score += 1
            print(f"You're right! Current score: {score}")
            a = b
            b = random.randint(0, size - 1)
            while a == b:
                b = random.randint(0, size - 1)
    else:
        if choice == "B":
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        else:
            score += 1
            print(f"You're right! Current score: {score}")
            b = random.randint(0, size - 1)
            while a == b:
                b = random.randint(0, size - 1)
