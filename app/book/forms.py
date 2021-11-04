from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import InputRequired

class AddBookForm(FlaskForm):
    ''' Form for adding a new book '''
    title = StringField('Title:', validators=[InputRequired()])
    author = StringField('Author:', validators=[InputRequired()])
    critics_rating = IntegerField('Critics Rating:', validators=[InputRequired()])
    genre_id = SelectField('Genre:', validators=[InputRequired()])
    submit = SubmitField('Add book')

class EditBookForm(AddBookForm):
    ''' Form for editing an existing book '''
    submit = SubmitField('Save changes')