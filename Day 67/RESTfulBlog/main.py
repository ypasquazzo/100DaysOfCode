from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt

from mail import Mail
CONTACT_MAIL = "xxxxxx"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
app.config['CKEDITOR_SERVE_LOCAL'] = True
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()], render_kw={'class': 'form-control'})
    subtitle = StringField(label="Subtitle", validators=[DataRequired()], render_kw={'class': 'form-control'})
    author = StringField(label="Your Name", validators=[DataRequired()], render_kw={'class': 'form-control'})
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()],
                          render_kw={'class': 'form-control'})
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


def get_posts():
    posts = []
    posts_db = BlogPost.query.all()

    for post in posts_db:
        blog_post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'date': post.date,
            'body': post.body,
            'author': post.author,
            'img_url': post.img_url
        }
        posts.append(blog_post)
    return posts


@app.route('/')
def get_all_posts():
    posts = get_posts()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = get_posts()
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['GET', 'POST'])
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, author=form.author.data,
                        img_url=form.img_url.data, body=form.body.data,
                        date=dt.today().strftime('%B %d, %Y'))
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)
    return render_template("make-post.html", form=form, edit=False)


@app.route("/edit-post/<post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    form = CreatePostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = BlogPost.query.get(post_id)
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('show_post', index=post.id))

    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    return render_template("make-post.html", form=edit_form, index=post.id, edit=True)


@app.route("/delete/<post_id>")
def delete(post_id):
    post = BlogPost.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


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


if __name__ == "__main__":
    app.run(debug=True)
