import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
length = len(chosen_word)
blanks = length
used = []
lives = 6

reveal = "["
for i in range(0, length-1):
    reveal += "\"_\","
reveal += "\"_\"]"

print(hangman_art.logo)
print(hangman_art.stages[lives])
print(reveal)

while blanks > 0:
    match = False

    while True:
        guess = input("What is your guess? ").lower()
        if used.count(guess) == 0:
            used.append(guess)
            break

    for i in range(0, length):
        if chosen_word[i] == guess:
            reveal = reveal[:4*i+2] + guess + reveal[4*i+3:]
            blanks -= 1
            match = True

    if not match:
        lives -= 1
    print(hangman_art.stages[lives])
    print(reveal)
    print(f"Already used letters: {used}")

    if lives == 0:
        print(f"You lose! The word was {chosen_word}...")
        break

if blanks == 0:
    print("You win!")
