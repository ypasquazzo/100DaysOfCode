from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    return f"<h1>Name: {request.form['username']}, Password: {request.form['username']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
