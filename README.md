# flask-boilerplate

Basic Flask app with Bootstrap, webassets, WTForms and social login


### What's this? ###

flask-boilerplate is a simple Flask app built on top of [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/), [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/), [Flask-Login](https://flask-login.readthedocs.org/en/latest/), [Authomatic](http://peterhudec.github.io/authomatic/) and [Flask-Assets](http://flask-assets.readthedocs.org/en/latest/) that you can use to jump-start that new project.

![flask-boilerplate screenshot](https://raw.githubusercontent.com/g4b1nagy/flask-boilerplate/master/screenshot.png)


### What can it do? ###

Specifically, flask-boilerplate comes with:

* Bootstrap-based layout
* asset bundles for LESS, CSS and JS
* flash message support
* WTForms example
* OAuth login with Facebook, Google+ and Twitter


### Getting your hands dirty ###

* cd to a comfy location
* git clone git@github.com:g4b1nagy/flask-boilerplate.git
* sudo npm install -g less
* sudo ln -s /usr/bin/nodejs /usr/bin/node  # in case you get "node: command not found" in bash
* cd flask-boilerplate/
* virtualenv -p $(which python3) venv
* source venv/bin/activate
* pip install -r requirements.txt
* cp config_example.py config.py
* update the config.py file to suit your needs
* ./manage.py db_create
* ./manage.py runserver
* point your browser to [http://localhost:5000/](http://localhost:5000/)
