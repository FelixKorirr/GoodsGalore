from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, provided_username):
        usr = User.query.filter_by(username=provided_username.data).first()
        if usr:
            raise ValidationError('username already exists')

    def validate_email(self, provided_email):
        usr = User.query.filter_by(email=provided_email.data).first()
        if usr:
            raise ValidationError('email already exists')

    username = StringField('Username:', validators=[
        Length(min=3, max=30), DataRequired()])
    email = StringField('Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField('Password:', validators=[
        Length(min=6), DataRequired()])
    confirm_password = PasswordField('Confirm Password:', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')
