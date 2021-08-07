from flask import render_template, url_for, flash, redirect, request
from covid import app, db, bcrypt
from covid.forms import RegistrationForm, LoginForm, ScheduleForm
from covid.models import User
from flask_login import login_user, current_user, logout_user, login_required
from utils import *
from SEIRmodel.refine_SEIR import SEIR
import datetime


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = ScheduleForm()
    if form.validate_on_submit():

        time = form.time.data
        location = form.location.data

        covid_num, recovered = province_covid_num(location)
        population = province_population(location)
        model = SEIR(population, covid_num, recovered, covid_num, time, risks)
        result = model.predict()
        numOfDays = date - presentDate
        if result[numOfDnumOfDays > 0 && result[numOfDays] - result > 5

        warnings.append("Your trip to " + event[locationIndex] + " on " + date + "may be dangerous")


    return render_template('home.html', form=form)


@app.route('/result')
def result():
    return render_template('result.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
