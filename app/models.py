from flask.ext.login import UserMixin

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    picture_url = db.Column(db.String(128))
    social_id = db.Column(db.String(128), unique=True)
    social_profile_url = db.Column(db.String(128))

    def __init__(self, first_name, last_name, email, picture_url, social_id, social_profile_url):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.picture_url = picture_url
        self.social_id = social_id
        self.social_profile_url = social_profile_url

    def __repr__(self):
        return 'User #{} - {} {}'.format(self.id, self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
