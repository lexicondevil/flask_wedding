from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
assets = Environment(app)

from app import views
from app import models