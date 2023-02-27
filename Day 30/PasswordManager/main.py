from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def create_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


def save_password():
    website = entry_website.get()
    username = entry_email_uname.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }

    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Make sure none of the fields are empty!")
        return

    confirmation = messagebox.askokcancel(title=website, message=f"You have entered: \nUsername: {username} "
                                                                 f"\nPassword: {password} \nIs it ok to save?")
    if confirmation:
        try:
            with open(file="data.json", mode="r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open(file="data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_email_uname.delete(0, END)
            entry_password.delete(0, END)


def find_password():
    website = entry_website.get()
    try:
        with open(file="data.json", mode="r") as f:
            data = json.load(f)
            try:
                username = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {username} \nPassword:{password}")
            except KeyError:
                messagebox.showinfo(title="Error", message=f"No credentials saved for {website}.")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data file found.")


# Useful info for layouts: https://riptutorial.com/tkinter/example/29713/grid--
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")

generate_btn = Button(text="Generate Password", command=create_pw)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
