import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.engine.url import make_url


app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"

DATABASE_URL = os.getenv('DATABASE_URL')

db_url = make_url(DATABASE_URL)

app.config[
    "SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'

# fmt: off
from market import routes
from market import models
# fmt:on