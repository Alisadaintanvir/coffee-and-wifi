from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 8AM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                         validators=[DataRequired()])
    wifi_strength = SelectField('Wifi Strength Rating', choices=['❌', '💪', '💪💪', '💪💪💪', '💪💪💪💪',
                                                                 '💪💪💪💪💪'], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=['❌', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌',
                                                              '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data, form.rating.data,
                    form.wifi_strength.data, form.power.data]
            with open('cafe-data.csv', mode='a', newline='', encoding='utf8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(data)
            print("True")
            print(data)
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
