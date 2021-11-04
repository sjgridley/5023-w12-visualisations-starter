from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class AddGenreForm(FlaskForm):
    ''' Form for adding a new genre '''
    name = StringField('Name:', validators=[InputRequired()])
    submit = SubmitField('Add genre')

class EditGenreForm(AddGenreForm):
    ''' Form for editing an existing genre '''
    submit = SubmitField('Save changes')
