#!/usr/bin/env python

from flask.ext.assets import ManageAssets
from flask.ext.script import Manager

from app import app, assets, db
from app.models import User


manager = Manager(app)
manager.add_command('assets', ManageAssets(assets))


@manager.command
def db_create():
    db.create_all()


@manager.command
def db_seed():
    user = User(
        first_name='Gabi',
        last_name='Nagy',
        email='gabi@helpfulsheep.com',
        picture_url='http://helpfulsheep.com/assets/helpful-sheep.png',
        social_id='facebook_12345',
        social_profile_url='http://helpfulsheep.com/',
    )
    db.session.add(user)
    db.session.commit()


@manager.command
def db_drop():
    db.drop_all()


if __name__ == '__main__':
    manager.run()
