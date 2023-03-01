import html


class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(question.text)}"

    def still_has_questions(self):
        return not self.question_number == len(self.question_list)

    def check_answer(self) -> bool:
        return self.question_list[self.question_number - 1].answer == "True"
