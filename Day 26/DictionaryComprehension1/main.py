# TODO: You are going to use Dictionary Comprehension to create a dictionary called {result} that
#  takes each word in the given sentence and calculates the number of letters in each word.
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}
print(result)
