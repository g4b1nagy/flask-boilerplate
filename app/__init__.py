# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.assets import Environment

from assets import css, js


app = Flask(__name__)
app.config.from_object('config')


assets = Environment(app)
assets.register('css', css)
assets.register('js', js)


from app import views
