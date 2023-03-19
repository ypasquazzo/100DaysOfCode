from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'xxxxxx'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)


# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html", logged_in=current_user.is_authenticated)

    user = User.query.filter_by(email=request.form['email']).first()
    if user is None:
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
        # noinspection PyArgumentList
        new_user = User(email=request.form['email'], password=password, name=request.form['name'])
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return render_template("secrets.html", name=new_user.name)
    else:
        flash(u'You already signed up with that account. Log in instead!', 'error')
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", logged_in=current_user.is_authenticated)

    password = request.form['password']
    user = User.query.filter_by(email=request.form['email']).first()
    if user is None:
        flash(u'This user does not exist.', 'error')
        return redirect(url_for('login'))

    if check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('secrets'))
    else:
        flash(u'Invalid password provided.', 'error')
        return redirect(url_for('login'))


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
def download():
    if not current_user.is_authenticated:
        abort(401, description="You must log in to access this page.")
    return send_from_directory("static", "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
