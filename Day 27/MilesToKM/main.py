from tkinter import *


def convert():
    label_3.config(text=round(float(entry.get()) * 1.60934, 1))


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=10)

entry = Entry(width=8)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="KM")
label_4.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=3, column=1)

window.mainloop()
