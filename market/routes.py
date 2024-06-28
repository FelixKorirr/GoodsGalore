from market import app
from market.models import Item
from flask import render_template, redirect, url_for, flash
from market.forms import RegisterForm, LoginForm
from market.models import User
from market import db
from flask_login import login_user, logout_user, login_required


@app.route("/")
@app.route("/home", strict_slashes=False)
def home():
    return render_template('home.html')


@app.route("/market", strict_slashes=False)
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=["GET", "POST"], strict_slashes=False)
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors:
        for field_name, errors in form.errors.items():
            for error in errors:
                flash(f"{field_name} field error: {error}", category="danger")
    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        usr = User.query.filter_by(email=form.email.data).first()
        if usr and usr.check_password(form.password.data):
            login_user(usr)
            flash('Login SuccessFul', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('username and password do not match', category='danger')

    return render_template("login.html", form=form)


@app.route("/logout", strict_slashes=False)
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home'))
