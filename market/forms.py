from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[
                           Length(min=2, max=30), DataRequired()])
    email = StringField('Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField('Password:', validators=[
                             Length(min=6), DataRequired()])
    confirm_password = PasswordField('Confirm Password:', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')
