from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LinkForm(FlaskForm):
    link = StringField('Link :', validators=[DataRequired()])
    submit = SubmitField('Sign In')
