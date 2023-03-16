from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# Create the DB once if not yet present:
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", books=db.session.query(Book).all())


@app.route('/delete')
def delete():
    book_to_delete = Book.query.filter_by(id=request.args.get('id')).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template("add.html")

    new_book = Book(title=request.form['name'], author=request.form['author'], rating=request.form['rating'])
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        return render_template('edit.html', book=Book.query.filter_by(id=request.args.get('id')).first())

    book_to_update = Book.query.filter_by(title=request.form['title']).first()
    book_to_update.rating = request.form['new_rating']
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
