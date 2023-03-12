from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


def bold(function):
    def bold_wrapper():
        return f"<b>{function()}</b>"
    return bold_wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/quit')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'


if __name__ == "__main__":
    app.run(debug=True)
