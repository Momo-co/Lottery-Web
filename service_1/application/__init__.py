from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SECRET_KEY = os.getenv("SECRET_KEY")
)


db = SQLAlchemy(app)

from . import routes