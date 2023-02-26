# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word to spell: ")
nato = [nato_dictionary[letter.upper()] for letter in word]
print(f"{word}: {nato}")
