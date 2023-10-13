# Write a program that simulate a silent auction and announces the winner.
# The screen must be cleared between each auction.
from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

new_participant = "yes"
participant = {}
bid = 0
winner = []

while new_participant == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid: $"))

    participant[name] = bid

    new_participant = input("Are there any other bidders? Type 'yes' or 'no': ")
    clear()

for key in participant:
    if participant[key] >= bid:
        winner.append(key)
        bid = participant[key]

if len(winner) == 1:
    print(f"The winner is {winner[0]} with a bid of ${participant[winner[0]]}.")
else:
    print(f"We have {len(winner)} tied winners: {winner} with a bid of ${participant[winner[0]]}.")
