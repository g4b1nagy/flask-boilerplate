#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from app import app


app.config['DEBUG'] = True
manager = Manager(app)


@manager.command
def hello():
  print 'Hello!'


if __name__ == '__main__':
  manager.run()
