# Write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
#
# DO NOT modify the List numbers directly.
# Try to use List Comprehension instead of a Loop.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers]
print(squared_numbers)
