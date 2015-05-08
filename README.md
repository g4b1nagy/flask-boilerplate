flask-boilerplate
=================

Basic Flask app

### What's this? ###

flask-boilerplate is a really simple Flask app built on top of [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/), [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/), [Flask-Login](https://flask-login.readthedocs.org/en/latest/), [Authomatic](http://peterhudec.github.io/authomatic/) and [Flask-Assets](http://flask-assets.readthedocs.org/en/latest/) that you can use to jump-start that new project.

![flask-boilerplate screenshot](https://raw.githubusercontent.com/g4b1nagy/flask-boilerplate/master/screenshot.png)

Specifically, flask-boilerplate comes with:

* Bootstrap-based layout
* asset bundles for LESS, CSS and JS
* flash message support
* WTForms example
* OAuth login with Facebook, Google+ and Twitter

### Getting your hands dirty ###

* cd to a comfy location
* git clone git@github.com:g4b1nagy/flask-boilerplate.git
* cd flask-boilerplate/
* virtualenv .venv
* source .venv/bin/activate
* pip install -r requirements.txt
* cp config_example.py config.py
* update the config.py file to suit your needs
* ./manage.py db_create
* ./manage.py runserver
* point your browser to [http://localhost:5000/](http://localhost:5000/)
