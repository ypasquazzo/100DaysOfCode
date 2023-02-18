# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

print(int(float(weight)/float(height)**2))