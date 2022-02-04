from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    pasword = PasswordField('Password', validators=[DataRequired()])
    confirm_pasword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    pasword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')