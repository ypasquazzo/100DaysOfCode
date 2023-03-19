from flask import Flask, render_template, request, url_for, redirect, flash, abort
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_gravatar import Gravatar
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
from datetime import datetime as dt
from functools import wraps

from mail import Mail
from form import CreatePostForm, RegisterForm, LoginForm, CommentForm

CONTACT_MAIL = "xxxxxx"

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'secret'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
app.config['CKEDITOR_SERVE_LOCAL'] = True
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comment_author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"), nullable=False)
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.Text, nullable=False)


db.create_all()


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


def admin_only(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.is_authenticated:
            if User.query.filter_by(email=current_user.email).first().id == 1:
                return function(*args, **kwargs)
        return abort(401)  # Unauthorized
    return wrapper_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def get_all_posts():
    posts = get_posts()
    user_id = 0
    if current_user.is_authenticated:
        user_id = User.query.filter_by(email=current_user.email).first().id
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, user_id=user_id)


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=form.body.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html", post=requested_post, form=form, current_user=current_user)


@app.route("/new-post", methods=['GET', 'POST'])
@admin_only
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, author=current_user,
                        img_url=form.img_url.data, body=form.body.data,
                        date=dt.today().strftime('%B %d, %Y'))
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)
    return render_template("make-post.html", form=form, edit=False, logged_in=current_user.is_authenticated)


@app.route("/edit-post/<post_id>", methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost.query.get(post_id)
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))

    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    return render_template("make-post.html", form=edit_form, index=post.id,
                           edit=True, logged_in=current_user.is_authenticated)


@app.route("/delete/<post_id>")
@admin_only
def delete(post_id):
    post = BlogPost.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
            # noinspection PyArgumentList
            new_user = User(email=form.email.data, password=password, name=form.name.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/")
        else:
            flash(u'You already signed up with that account. Log in instead!', 'error')
            return redirect(url_for('login'))

    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(u'This user does not exist.', 'error')
            return redirect(url_for('login'))

        password = form.password.data
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
        else:
            flash(u'Invalid password provided.', 'error')
            return redirect(url_for('login'))

    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", contact=False, logged_in=current_user.is_authenticated)
    else:
        mail = Mail()
        mail.send_message(CONTACT_MAIL, "New message from the Blog",
                          f"From: {request.form['name']} \nPhone: {request.form['phone']} \n"
                          f"Email: {request.form['email']} \nMessage: {request.form['message']}")
        return render_template("/contact.html", contact=True)


if __name__ == "__main__":
    app.run(debug=True)
