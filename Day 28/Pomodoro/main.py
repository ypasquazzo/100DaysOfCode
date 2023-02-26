from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
marks = ""


def reset():
    global marks, timer, reps
    
    window.after_cancel(str(timer))
    label_head.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    marks = ""
    label_tick.config(text=marks, fg=GREEN)
    reps = 0


def start_timer():
    global reps

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 != 0:
        label_head.config(text="Work", fg=GREEN)
        count_down(work_time)
    elif reps % 8 == 0:
        label_head.config(text="Break", fg=RED)
        count_down(long_break_time)
    else:
        label_head.config(text="Break", fg=PINK)
        count_down(short_break_time)


def count_down(time):
    global timer, reps, marks

    minutes = int(time / 60)
    seconds = time % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        timer = window.after(1000, count_down, time-1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks += "✔"
            label_tick.config(text=marks, fg=GREEN)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_head = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
label_head.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(row=2, column=2)

label_tick = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
label_tick.grid(row=3, column=1)

window.mainloop()
