from tkinter import *

import data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
LANGUAGE_FONT = ("Arial", 20, "italic")
count: int


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.count = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score: 0", padx=20, bg=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=275, fill=THEME_COLOR,
                                                     text="TEST", font=LANGUAGE_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        right_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=right_image, highlightthickness=0, command=self.check_if_true)
        self.button_true.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=wrong_image, highlightthickness=0, command=self.check_if_false)
        self.button_false.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.reset_to_white()
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quizz. \n"
                                                            f"Score: {self.count}" + "/" + str(data.NB_QUESTIONS))

    def check_if_true(self):
        if self.quiz.check_answer():
            self.colour_effect("green")
        else:
            self.colour_effect("red")

    def check_if_false(self):
        if self.quiz.check_answer():
            self.colour_effect("red")
        else:
            self.colour_effect("green")

    def colour_effect(self, colour: str):
        self.canvas.config(bg=colour)
        self.window.after(1000, self.reset_to_white)
        if colour == "green":
            self.count += 1
            self.label_score.config(text=f"Score: {self.count}")
        self.next_question()

    def reset_to_white(self):
        self.canvas.config(bg="white")
