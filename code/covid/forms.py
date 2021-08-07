from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from covid.models import User

choices = [
    ('1', 'Beijing'),
    ('2', 'Tianjin'),
    ('3', 'Shanghai'),
    ('4', 'Chongqing'),
    ('5', 'Hebei'),
    ('6', 'Shanxi'),
    ('7', 'Liaoning'),
    ('8', 'Jilin'),
    ('9', 'Heilongjiang'),
    ('10', 'Jiangsu'),
    ('11', 'Zhejiang'),
    ('12', 'Anhui'),
    ('13', 'Fujian'),
    ('14', 'Jiangxi'),
    ('15', 'Shandong'),
    ('16', 'Henan'),
    ('17', 'Hubei'),
    ('18', 'Hunan'),
    ('19', 'Guangdong'),
    ('20', 'Hainan'),
    ('21', 'Sichuan'),
    ('22', 'Guizhou'),
    ('23', 'Yunnan'),
    ('24', 'Shanxi'),
    ('25', 'Gansu'),
    ('26', 'Qinghai'),
    ('27', 'Inner Mongolia'),
    ('28', 'Guangxi'),
    ('29', 'Tibet'),
    ('30', 'Ningxia'),
    ('31', 'Xinjiang')
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
