from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange
import requests

TMDB_API_KEY = "xxxxxx"
TMDB_URL = "https://api.themoviedb.org/3/"

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


class MovieForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired(),
                                                                            NumberRange(min=0.0, max=10.0)])
    review = StringField(label='Your Review', validators=[DataRequired()])
    movie_id = HiddenField(label='Movie ID')
    submit = SubmitField(label='Submit')


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    if movies is not None:
        ranking = 1
        for movie in movies:
            Movie.query.filter_by(id=movie.id).first().ranking = ranking
            db.session.commit()
            ranking += 1

    return render_template("index.html", movies=db.session.query(Movie).order_by(Movie.ranking.desc()).limit(10).all())


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = MovieForm()
    if form.validate_on_submit():
        movie_to_update = Movie.query.filter_by(id=form.movie_id.data).first()
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie_id=Movie.query.filter_by(id=request.args.get('id')).first().id, form=form)


@app.route('/delete')
def delete():
    movie_to_delete = Movie.query.filter_by(id=request.args.get('id')).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_list = []
        parameters = {"api_key": TMDB_API_KEY, "query": form.title.data}
        response = requests.get(url=f"{TMDB_URL}search/movie?", params=parameters)
        response.raise_for_status()
        data = response.json()
        for movie in data["results"]:
            item = {"id": movie["id"],
                    "title": movie["original_title"],
                    "year": movie["release_date"][:4]}
            movie_list.append(item)
        print(movie_list)
        return render_template('select.html', movies=movie_list)

    return render_template('add.html', form=form)


@app.route("/<tmdb_id>")
def movie_chosen(tmdb_id):
    form = MovieForm()
    parameters = {"api_key": TMDB_API_KEY}
    response = requests.get(url=f"{TMDB_URL}movie/{tmdb_id}?", params=parameters)
    response.raise_for_status()
    data = response.json()

    new_movie = Movie(
        title=data["original_title"],
        year=data["release_date"][:4],
        description=data["overview"],
        rating=0,
        ranking=-1,
        review="No review.",
        img_url="https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return render_template('edit.html',
                           movie_id=Movie.query.filter_by(title=data["original_title"]).first().id,
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)
