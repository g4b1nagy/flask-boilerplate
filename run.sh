#!/bin/bash


killall -9 uwsgi
uwsgi --module app:app --home /var/www/flask-boilerplate/venv/ --socket /tmp/uwsgi.sock --chmod-socket=666 --master --workers 4 --logto /tmp/uwsgi.log
