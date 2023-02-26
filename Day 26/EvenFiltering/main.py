#  write a List Comprehension to create a new list called result.
#  This new list should only contain the even numbers from the list numbers.
#
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
