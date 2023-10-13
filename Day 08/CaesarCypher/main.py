# Write a program that implements the Caesar Cypher.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
play = "yes"
print(art.logo)


def caesar(t, s, d):
    s = s % 26
    if d == "decode":
        s = -s

    message = ""
    for c in range(0, len(t)):
        if t[c] not in alphabet:
            message += t[c]
            break
        message += alphabet[alphabet.index(t[c]) + s]
    return message


while play == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(text, shift, direction))

    play = input("Do you want to play again? (yes/no) ")
