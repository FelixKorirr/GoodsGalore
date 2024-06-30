from market import app
from market.models import Item
from flask import render_template, redirect, url_for, flash, request
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market.models import User
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home", strict_slashes=False)
def home():
    return render_template('home.html')


@app.route("/market", methods=["GET", "POST"], strict_slashes=False)
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if request.method == "POST":
        # Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        p_item = Item.query.filter_by(name=purchased_item).first()
        if p_item:
            if current_user.budget > p_item.price:
                p_item.owner_id = current_user.id
                current_user.budget -= p_item.price
                db.session.commit()
                flash(
                    f"Congratulations! You have purchased {p_item.name}", category='success')
            else:
                flash(
                    f"Unfortunately, you don't have enough funds to purchase {p_item.name}", category='danger')
        # Sell Item Logic
        sold_item = request.form.get('name')
        s_item = Item.query.filter_by(name=sold_item).first()
        if s_item:
            s_item.owner_id = None
            current_user.budget += s_item.price
            db.session.commit()
            flash(
                f"Congratulations, you've successfully sold {s_item.name}", category="success")

        return redirect(url_for('market_page'))
    elif request.method == "GET":
        items = Item.query.filter_by(owner_id=None).all()
        owned_items = Item.query.filter_by(owner_id=current_user.id).all()
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, sell_form=sell_form)


@app.route("/register", methods=["GET", "POST"], strict_slashes=False)
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful', category='success')
        return redirect(url_for('login_page'))

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
