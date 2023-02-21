# ############## Blackjack Project #####################

# Difficulty Normal     [ ]: Use all Hints below to complete the project.
# Difficulty Hard       [ ]: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard [ ]: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert     [X]: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules ################

# * The deck is unlimited in size.
# * There are no jokers.
# * The Jack/Queen/King all count as 10.
# * The Ace can count as 11 or 1.
# * Use the following list as the deck of cards:
#      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# * The cards in the list have equal probability of being drawn.
# * Cards are not removed from the deck as they are drawn.
# * The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import os
import random

import art

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return cards[random.randint(0, 12)]


def get_score(hand):
    score = 0
    for c in hand:
        score += c
    return score


def check_aces(h):
    if h.count(11) > 0 and get_score(h) > 21:
        h[h.index(11)] = 1


def print_current_hand(p, c):
    print(f"Your cards: {p}, current score: {get_score(p)}")
    print(f"Computer's first card: {c[0]}")


def print_final_hand(p, c):
    print(f"Your final hand: {p}, final score: {get_score(p)}")
    print(f"Computer's final hand: {c}, final score: {get_score(c)}")


while play == 'y':
    os.system('cls')
    print(art.logo)

    player = []
    computer = []

    player.append(draw_card())
    player.append(draw_card())
    check_aces(player)
    computer.append(draw_card())
    computer.append(draw_card())
    check_aces(computer)

    print_current_hand(player, computer)
    card = input("Type 'y' to get another card, type 'n' to pass: ")

    while card == 'y':
        player.append(draw_card())
        check_aces(player)
        print_current_hand(player, computer)
        if get_score(player) > 21:
            break
        card = input("Type 'y' to get another card, type 'n' to pass: ")

    while get_score(computer) < 17:
        computer.append(draw_card())
        check_aces(computer)
    if get_score(computer) < get_score(player) <= 21:
        computer.append(draw_card())
        check_aces(computer)

    print_final_hand(player, computer)

    if get_score(player) > 21:
        if get_score(computer) <= 21:
            print("You went over. You loose!")
            if get_score(computer) == 21:
                print("Opponent has Blackjack!")
        else:
            print("You both went over. That's a draw!")
    if get_score(player) <= 21:
        if get_score(computer) > 21:
            if get_score(player) == 21:
                print("Opponent went over. You win with a Blackjack!")
            else:
                print("Opponent went over. You win!")
        elif get_score(player) == get_score(computer):
            if get_score(computer) == 21:
                print("Blackjack! But that's a draw...")
            else:
                print("Draw!")
        else:
            if get_score(computer) == 21:
                print("You lose, opponent has Blackjack!")
            else:
                print("You lose!")

    play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
