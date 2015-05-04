#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.assets import ManageAssets

from app import app, assets, db
from app.models import User


app.config['DEBUG'] = True
manager = Manager(app)


manager.add_command('assets', ManageAssets(assets))


@manager.command
def db_create():
  db.create_all()


@manager.command
def db_seed():
  user = User('Gabi Nagy', 'gabi@helpfulsheep.com')
  db.session.add(user)
  db.session.commit()


@manager.command
def db_drop():
  db.drop_all()


if __name__ == '__main__':
  manager.run()
