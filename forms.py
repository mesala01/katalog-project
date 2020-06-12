from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo, Email

class SignupForm(FlaskForm):
    """
        generates the signup form
    """
    name = StringField('Name', validators=[InputRequired("Enter your fullname")])
    email = StringField('Email', validators =[InputRequired("Enter a valida email"), Email()])
    password = PasswordField('New Password', validators= [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Confirm Password')
    #recaptcha = RecaptchaField()


class LoginForm(FlaskForm):
    """
        generate login form
    """
    email = StringField('Email', validators =[InputRequired("Enter a valida email"), Email()])
    password = PasswordField('New Password', validators= [InputRequired()])









