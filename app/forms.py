# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(Form):
  name = StringField('Name', description='Name', validators=[DataRequired(message="You're not listening, are you?")])
