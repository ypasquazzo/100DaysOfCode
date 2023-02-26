# TODO: Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# IMPORTANT: The result should be a list that contains Integers, not Strings.
# Try to use List Comprehension instead of a Loop.

with open(file="file1.txt", mode="r") as f1:
    file1 = f1.readlines()

with open(file="file2.txt", mode="r") as f2:
    file2 = f2.readlines()

result = [int(n) for n in file1 if n in file2]
print(result)
