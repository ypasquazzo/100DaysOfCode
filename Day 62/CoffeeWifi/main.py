from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

COFFEE_ICON = [('0', '☕️'), ('1', '☕️☕️'), ('2', '☕️☕️☕️'), ('3', '☕️☕️☕️☕️'), ('4', '☕️☕️☕️☕️☕️')]
STRENGTH_ICON = [('0', '✘'), ('1', '💪'), ('2', '💪💪'), ('3', '💪💪💪'), ('4', '💪💪💪💪'), ('5', '💪💪💪💪💪')]
POWER_ICON = [('0', '✘'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌')]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxxxx'
Bootstrap(app)


class CafeForm(FlaskForm):
    name = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    o_time = StringField(label='Opening Time e.g. 5:30AM', validators=[DataRequired()])
    c_time = StringField(label='Closing Time e.g. 8PM', validators=[DataRequired()])
    coffe_rating = SelectField(label='Coffee Rating', choices=COFFEE_ICON)
    strength_rating = SelectField(label='Wi-Fi Strength Rating', choices=STRENGTH_ICON)
    power_rating = SelectField(label='Power Socket Availability', choices=POWER_ICON)
    submit = SubmitField(label='Submit', render_kw={'class': 'btn-style'})


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [form.name.data, form.location.data, form.o_time.data, form.c_time.data,
                   COFFEE_ICON[int(form.coffe_rating.data)][1], STRENGTH_ICON[int(form.strength_rating.data)][1],
                   POWER_ICON[int(form.power_rating.data)][1]]
        with open("cafe-data.csv", mode="a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        return redirect('add')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
