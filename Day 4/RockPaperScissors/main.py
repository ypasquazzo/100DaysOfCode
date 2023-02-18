# Build a Rock/Paper/Scissors game.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play Rock/Paper/Scissors!\n")
choices = ["Rock", "Paper", "Scissors"]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(f"You are playing {choices[player]}:")

computer = random.randint(0, 2)

if player == 0:
    print(rock)
    if computer == 0:
        print(f"The computer is playing {choices[computer]}:")
        print(rock)
        print("This is a draw!")
    elif computer == 1:
        print(f"The computer is playing {choices[computer]}:")
        print(paper)
        print("You loose!")
    elif computer == 2:
        print(f"The computer is playing {choices[computer]}:")
        print(scissors)
        print("You win!")
if player == 1:
    print(paper)
    if computer == 0:
        print(f"The computer is playing {choices[computer]}:")
        print(rock)
        print("You win!")
    elif computer == 1:
        print(f"The computer is playing {choices[computer]}:")
        print(paper)
        print("This is a draw!")
    elif computer == 2:
        print(f"The computer is playing {choices[computer]}:")
        print(scissors)
        print("You loose!")
if player == 2:
    print(scissors)
    if computer == 0:
        print(f"The computer is playing {choices[computer]}:")
        print(rock)
        print("You loose!")
    elif computer == 1:
        print(f"The computer is playing {choices[computer]}:")
        print(paper)
        print("You win!")
    elif computer == 2:
        print(f"The computer is playing {choices[computer]}:")
        print(scissors)
        print("This is a draw!")
