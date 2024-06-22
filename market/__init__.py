import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"
database_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'market.db')

app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{database_path}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from market import routes
from market import models
