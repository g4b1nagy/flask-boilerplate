from authomatic import Authomatic
from flask import Flask
from flask_assets import Environment
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

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


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


from app import views
