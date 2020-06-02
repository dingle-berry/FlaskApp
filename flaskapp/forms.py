from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskapp.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username',
                         validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password_confirm = PasswordField('Password Confirm', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
      user = User.query.filter_by(username=username.data).first()
      if user:
          raise ValidationError('Username already in use.')

  def validate_email(self, email):
      check_email = User.query.filter_by(email=email.data).first()
      if check_email:
          raise ValidationError('An account with this email already exists. Try logging in?')

class LoginForm(FlaskForm):
  username = StringField('Username',
                         validators=[DataRequired(), Length(min=2, max=20)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign in')
  remember = BooleanField('Remember Me')

class UpdateAccountForm(FlaskForm):
  username = StringField('Username',
                         validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
  submit = SubmitField('Update')

  def validate_username(self, username):
      if username.data != current_user.username:
        user = User.query.filter_by(username=username.data).first()
        if user:
              raise ValidationError('Username already in use.')

  def validate_email(self, email):
      if email.data != current_user.email:
        check_email = User.query.filter_by(email=email.data).first()
        if check_email:
              raise ValidationError('An account with this email already exists. Try logging in?')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
