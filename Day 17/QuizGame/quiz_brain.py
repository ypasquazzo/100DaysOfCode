class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f"Q.{self.question_number}: {question.text} True/False?: ")

    def still_has_questions(self):
        return not self.question_number == len(self.question_list)

    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number-1].answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number-1].answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
