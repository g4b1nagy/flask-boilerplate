# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for
from flask.ext.login import login_required

from app import app, login_manager
from forms import MyForm
from models import User

# =========================================================================
# Flask-Login
# =========================================================================

@login_manager.user_loader
def load_user(id):
  user = User.query.filter_by(id=id)
  return user


@login_manager.unauthorized_handler
def unauthorized():
  flash('You need to log in first.', 'warning')
  return redirect(url_for('login', next=request.url))

# =========================================================================
# App pages
# =========================================================================

@app.route('/', methods=('GET', 'POST'))
def index():
  form = MyForm()
  if form.validate_on_submit():
    return render_template('index.html', name=form.name.data)
  return render_template('index.html', form=form)


@app.route('/secret')
@login_required
def secret():
  return render_template('secret.html')


@app.route('/login')
def login():
  return render_template('login.html')

# =========================================================================
# Error pages
# =========================================================================

@app.errorhandler(404)
def error_404(error):
  return (render_template('404.html'), 404)


@app.errorhandler(500)
def error_500(error):
  return (render_template('500.html'), 500)
