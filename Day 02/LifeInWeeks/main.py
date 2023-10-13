# Create a program using maths and f-Strings that tells us how many days, weeks, months
# we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
#
#           You have x days, y weeks, and z months left.

age = input("What is your current age? ")

years_left = 90 - int(age)

print(f"You have {years_left*365} days, {years_left*52} weeks, and {years_left*12} months left.")