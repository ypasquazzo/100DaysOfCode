# The objective is to take the inputs from the user to these questions and then generate a random password.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
size = nr_letters + nr_numbers + nr_symbols
for i in range(0, size):
    if nr_letters > 0:
        password += letters[random.randint(0, len(letters)-1)]
        nr_letters -= 1
    elif nr_symbols > 0:
        password += symbols[random.randint(0, len(symbols)-1)]
        nr_symbols -= 1
    else:
        password += numbers[random.randint(0, len(numbers)-1)]
print(f"Easy password: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = ""
for i in range(0, size):
    n = random.randint(0, len(password)-1)
    password_hard += password[n]
    password = password.replace(password[n], "", 1)
print(f"Hard password: {password_hard}")
