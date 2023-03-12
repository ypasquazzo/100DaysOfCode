from flask import Flask
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'black']

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="400" height="400">'


@app.route('/<number>')
def check_number(number):
    if int(number) < random_number:
        return f'<h1 style="color: {COLORS[int(number)]};">Too low, try again!</h1>' \
               '<img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="400" height="400">'
    elif int(number) > random_number:
        return f'<h1 style="color: {COLORS[int(number)]};">Too high, try again!</h1>' \
               '<img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="400" height="400">'
    else:
        return f'<h1 style="color: {COLORS[int(number)]};">You found me!</h1>' \
               '<img src="https://i.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="400" height="400">'


if __name__ == "__main__":
    app.run(debug=True)
