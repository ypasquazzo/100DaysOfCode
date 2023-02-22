import data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for item in data.question_data:
    questions.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.check_answer(quiz.next_question())

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}!")
