from market import app
from market.models import Item
from flask import render_template, redirect, url_for, flash
from market.forms import RegisterForm
from market.models import User
from market import db
import time


@app.route("/")
@app.route("/home", strict_slashes=False)
def home():
    return render_template('home.html')


@app.route("/market", strict_slashes=False)
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=["GET", "POST"], strict_slashes=False)
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data, password_hash=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors:
        for err in form.errors.values():
            flash(err)

    return render_template('register.html', form=form)
