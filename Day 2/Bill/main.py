# Given a bill amount and a tip percentage, calculate how much each person needs to pay.
# The result must be rounded to the second decimal

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round((total/num) * (1+tip/100), 2)}")
