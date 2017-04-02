from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(EmailPasswordForm):
    confirmPass = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password',message='Passwords do not match')])


class LoginForm(EmailPasswordForm):
    pass
