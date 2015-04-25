#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.assets import ManageAssets

from app import app
from app import assets


app.config['DEBUG'] = True
manager = Manager(app)


@manager.command
def hello():
  print 'Hello!'


manager.add_command('assets', ManageAssets(assets))


if __name__ == '__main__':
  manager.run()
