from flask import Flask, render_template
import datetime as dt

from post import Post

AUTHOR = "Yannick P."

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", posts=posts_object, author=AUTHOR, date=date)


@app.route('/about.html')
def about():
    return render_template("/about.html")


@app.route('/contact.html')
def contact():
    return render_template("/contact.html")


@app.route('/post/<number>')
def post(number):
    id_int = int(number) - 1
    return render_template("post.html", post=posts_object[id_int], author=AUTHOR, date=date)


if __name__ == "__main__":
    posts_object = Post().posts
    date = dt.datetime.now().strftime("%B %d, %Y")
    app.run(debug=True)
