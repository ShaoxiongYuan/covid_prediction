from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from covid.models import User

choices = [
    ('Beijing', 'Beijing'),
    ('Tianjin', 'Tianjin'),
    ('Shanghai', 'Shanghai'),
    ('Chongqing', 'Chongqing'),
    ('Hebei', 'Hebei'),
    ('Shanxi', 'Shanxi'),
    ('Liaoning', 'Liaoning'),
    ('Jilin', 'Jilin'),
    ('Heilongjiang', 'Heilongjiang'),
    ('Jiangsu', 'Jiangsu'),
    ('Zhejiang', 'Zhejiang'),
    ('Anhui', 'Anhui'),
    ('Fujian', 'Fujian'),
    ('Jiangxi', 'Jiangxi'),
    ('Shandong', 'Shandong'),
    ('Henan', 'Henan'),
    ('Hubei', 'Hubei'),
    ('Hunan', 'Hunan'),
    ('Guangdong', 'Guangdong'),
    ('Hainan', 'Hainan'),
    ('Sichuan', 'Sichuan'),
    ('Guizhou', 'Guizhou'),
    ('Yunnan', 'Yunnan'),
    ('Shanxi', 'Shanxi'),
    ('Gansu', 'Gansu'),
    ('Qinghai', 'Qinghai'),
    ('Inner Mongolia', 'Inner Mongolia'),
    ('Guangxi', 'Guangxi'),
    ('Tibet', 'Tibet'),
    ('Ningxia', 'Ningxia'),
    ('Xinjiang', 'Xinjiang')
]


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ScheduleForm(FlaskForm):
    time = DateField('Time', validators=[DataRequired()])
    location = SelectField('Location', validators=[DataRequired()],
                           choices=choices)
    submit = SubmitField('submit')
