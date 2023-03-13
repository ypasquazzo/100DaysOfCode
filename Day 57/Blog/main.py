from flask import Flask, render_template

from post import Post

app = Flask(__name__)
posts_object = Post()


@app.route('/')
def hello_world():
    return render_template("index.html", posts=posts_object.posts)


@app.route('/post/<number>')
def get_blog(number):
    return render_template("post.html", posts=posts_object.posts, number=int(number))


if __name__ == "__main__":
    app.run(debug=True)
