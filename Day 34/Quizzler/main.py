import data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizzInterface


questions = []
for item in data.question_data["results"]:
    questions.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(questions)
ui = QuizzInterface(quiz)
