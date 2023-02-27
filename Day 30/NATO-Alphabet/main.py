import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


def enter_word():
    try:
        word = input("Enter a word to spell: ")
        nato = [nato_dictionary[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters of the alphabet please..")
        enter_word()
    else:
        print(f"{word}: {nato}")


enter_word()
