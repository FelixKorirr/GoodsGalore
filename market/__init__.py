import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"

database_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'market.db')

app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{database_path}'
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