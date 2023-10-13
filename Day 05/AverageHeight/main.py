# You are going to write a program that calculates the average student height from a List of heights.
#
# ex: 180 124 165 173 189 169 146

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

average = 0
for h in student_heights:
    average += h
average /= len(student_heights)

print(round(average))
