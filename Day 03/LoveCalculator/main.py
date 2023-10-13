# Write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
#   1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#   2. Then check for the number of times the letters in the word LOVE occurs.
#   3. Then combine these numbers to make a 2-digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#   "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#   "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#   "Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count_T = 0
count_R = 0
count_U = 0
count_E = 0

count_L = 0
count_O = 0
count_V = 0
count_E2 = 0

for i, v in enumerate((name1+name2).upper()):
    if v == "T":
        count_T += 1
    if v == "R":
        count_R += 1
    if v == "U":
        count_U += 1
    if v == "E":
        count_E += 1
    if v == "L":
        count_L += 1
    if v == "O":
        count_O += 1
    if v == "V":
        count_V += 1
    if v == "E":
        count_E2 += 1

love_score = (count_T+count_R+count_U+count_E) * 10 + (count_L+count_O+count_V+count_E2)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
