from flask.ext.login import UserMixin

from app import db


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  email = db.Column(db.String(128))

  def __init__(self, name, email):
    self.name = name
    self.email = email
