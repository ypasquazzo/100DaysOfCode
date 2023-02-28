from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
WAIT_TIME = 5000
data = None


def new_card():
    canvas.itemconfig(language_text, fill="black", text="Italian")
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(word_text, fill="black", text=random.choice(words))
    window.after(WAIT_TIME, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_text, fill="white", text="French")
    row = data[data["Italian"] == canvas.itemcget(word_text, "text")]
    canvas.itemconfig(word_text, fill="white", text=row["French"].values[0])


def validate_word():
    global data
    if canvas.itemcget(language_text, "text") == "Italian":
        messagebox.showerror(title="Error", message="Please wait for the French card to validate.")
    else:
        data = data.drop(data[data["French"] == canvas.itemcget(word_text, "text")].index)
        data.to_csv('data/words_to_learn.csv', index=False)
        new_card()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/italian_words.csv")
finally:
    words = data["Italian"].to_list()

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button = Button(image=right_image, highlightthickness=0, command=validate_word)
button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
button = Button(image=wrong_image, highlightthickness=0, command=new_card)
button.grid(row=1, column=1)

new_card()
mainloop()
