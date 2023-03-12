from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/quit')
def say_bye():
    return 'Bye, bye!'


if __name__ == "__main__":
    app.run()

