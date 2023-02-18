# Write a program that calculates the highest score from a List of scores.
#
# ex: 78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = 0
for s in student_scores:
    if s > max_score:
        max_score = s
print(f"The highest score in the class is: {max_score}")
