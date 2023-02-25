# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAMES_PATH = "Input/Names/invited_names.txt"
LETTER_PATH = "Input/Letters/starting_letter.txt"
READY_PATH = "Output/ReadyToSend/"


def read_names(path):
    with open(path, "r") as file:
        return file.readlines()


def read_letter(path):
    with open(path, "r") as file:
        return file.readlines()


def write_letter(path, name, content):
    for c in content:
        with open(path+"letter_for_"+name+".txt", "a") as file:
            file.write(c)


names = read_names(NAMES_PATH)
letter = read_letter(LETTER_PATH)

for i in range(0, len(names)):
    names[i] = names[i][:-1]

    temp = [letter[0].replace("[name]", names[i])]
    for part in letter[1:]:
        temp.append(part)

    print(temp)
    write_letter(READY_PATH, names[i], temp)
