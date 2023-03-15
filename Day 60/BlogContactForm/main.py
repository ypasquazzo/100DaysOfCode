from flask import Flask, render_template, request
import datetime as dt

from post import Post
from mail import Mail

AUTHOR = "Yannick P."
CONTACT_MAIL = "xxxxxx"

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", posts=posts_object, author=AUTHOR, date=date)


@app.route('/about')
def about():
    return render_template("/about.html")


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("/contact.html", contact=False)
    else:
        mail = Mail()
        mail.send_message(CONTACT_MAIL, "New message from the Blog",
                          f"From: {request.form['name']} \nPhone: {request.form['phone']} \n"
                          f"Email: {request.form['email']} \nMessage: {request.form['message']}")
        return render_template("/contact.html", contact=True)


@app.route('/post/<number>')
def post(number):
    id_int = int(number) - 1
    return render_template("post.html", post=posts_object[id_int], author=AUTHOR, date=date)


if __name__ == "__main__":
    posts_object = Post().posts
    date = dt.datetime.now().strftime("%B %d, %Y")
    app.run(debug=True)
