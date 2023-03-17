from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import random as rd
import locale

app = Flask(__name__)

locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route('/random', methods=['GET'])
def random_cafe():
    rd_cafe = rd.choice(Cafe.query.all())
    cafe_json = {column.name: getattr(rd_cafe, column.name) for column in rd_cafe.__table__.columns}
    return jsonify(cafe=cafe_json)


@app.route('/all', methods=['GET'])
def all_cafes():
    cafes = Cafe.query.all()
    cafes_json = []
    for cafe in cafes:
        cafes_json.append({column.name: getattr(cafe, column.name) for column in cafe.__table__.columns})
    return jsonify(cafes=cafes_json)


@app.route('/search', methods=['GET'])
def search_cafe():
    print(request.args.get('loc'))
    cafes = Cafe.query.filter_by(location=request.args.get('loc')).all()

    if cafes:
        cafes_json = []
        for cafe in cafes:
            cafes_json.append({column.name: getattr(cafe, column.name) for column in cafe.__table__.columns})
        return jsonify(cafes=cafes_json)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    

@app.route('/add', methods=['POST'])
def add_cafes():
    try:
        new_cafe = Cafe(name=request.form.get('name'), map_url=request.form.get('map_url'),
                        img_url=request.form.get('img_url'), location=request.form.get('location'),
                        seats=request.form.get('seats'), has_toilet=bool(request.form.get('has_toilet')),
                        has_wifi=bool(request.form.get('has_wifi')), has_sockets=bool(request.form.get('has_sockets')),
                        can_take_calls=bool(request.form.get('can_take_calls')),
                        coffee_price=request.form.get('coffee_price'))
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe"})

    except SQLAlchemyError:
        return jsonify(response={"error": "Failed to add new cafe."})


@app.route('/update-price/<id_cafe>', methods=['PATCH'])
def patch_cafe(id_cafe):
    try:
        cafe = Cafe.query.filter_by(id=id_cafe).first()
        cafe.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(response={"success": f"Successfully updated the cafe price to {request.form.get('new_price')}"})

    except SQLAlchemyError:
        return jsonify(response={"error": "Failed to update the coffee price."})
    except AttributeError:
        return jsonify(response={"error": "Sorry, a cafe with that ID was not found in the database."})


@app.route('/report-closed/<id_cafe>', methods=['DELETE'])
def delete(id_cafe):
    if request.form.get('api-key') == "TopSecretAPIKey":
        try:
            cafe = Cafe.query.filter_by(id=id_cafe).first()
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted the cafe."})

        except SQLAlchemyError:
            return jsonify(response={"error": "Failed to delete the cafe."})
        except AttributeError:
            return jsonify(response={"error": "Sorry, a cafe with that ID was not found in the database."})
    else:
        return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})


if __name__ == '__main__':
    app.run(debug=True)
