# -*- coding: utf-8 -*-

from authomatic import Authomatic
from flask import Flask
from flask.ext.assets import Environment
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from .assets import css, js


app = Flask(__name__)
app.config.from_object('config')


assets = Environment(app)
assets.register('css', css)
assets.register('js', js)


authomatic = Authomatic(app.config['AUTHOMATIC'], app.config['SECRET_KEY'])


db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


from app import views
