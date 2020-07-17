from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class AddMovieForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    cast = StringField('Star Cast (Comma Separated): ', validators=[DataRequired()])
    genre = StringField('Genre: ', validators=[DataRequired()])
    rating = IntegerField('Rating')
    comment = TextAreaField('Additional Comment(s): ')
    submit = SubmitField('Submit')


class SearchMovieForm(FlaskForm):
    name = StringField('Name: ')
    cast = StringField('Star Cast (Comma Separated): ')
    genre = StringField('Genre: ')
    submit = SubmitField('Search')
