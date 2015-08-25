# -*- coding: utf-8 -*-

from authomatic.adapters import WerkzeugAdapter
from flask import flash, make_response, redirect, render_template, request, session, url_for
from flask.ext.login import login_required, login_user, logout_user

from app import app, authomatic, db, login_manager
from .forms import MyForm
from .models import User

# =========================================================================
# Flask-Login
# =========================================================================

@login_manager.user_loader
def load_user(id):
  user = User.query.filter_by(id=id).first()
  return user


@login_manager.unauthorized_handler
def unauthorized():
  flash('You need to log in first.', 'warning')
  session['next_url'] = request.url
  return redirect(url_for('login', next=request.url))

# =========================================================================
# Authomatic
# =========================================================================

@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/login/<provider_name>', methods=('GET', 'POST'))
def social_login(provider_name):
  response = make_response()
  result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
  if result:
    if result.user:
      result.user.update()
      social_id = '{}_{}'.format(result.provider.name, result.user.id)
      user = User.query.filter_by(social_id=social_id).first()
      if user is None:
        # fix oauth inconsistencies
        if result.provider.name == 'facebook':
          result.user.picture = result.user.picture.replace('None', result.user.id)
        elif result.provider.name == 'twitter':
          result.user.first_name = result.user.name.split(' ')[0]
          result.user.last_name = result.user.name.split(' ')[1]
        user = User(
          first_name=result.user.first_name,
          last_name=result.user.last_name,
          email=result.user.email,
          picture_url=result.user.picture,
          social_id=social_id,
          social_profile_url=result.user.link,
        )
        db.session.add(user)
        db.session.commit()
      login_user(user, remember=True)
    elif result.error:
      flash(result.error.message, 'danger')
      return redirect(url_for('login'))
    return redirect(session.pop('next_url', url_for('secret')))
  return response


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

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

# =========================================================================
# Error pages
# =========================================================================

@app.errorhandler(404)
def error_404(error):
  return (render_template('404.html'), 404)


@app.errorhandler(500)
def error_500(error):
  return (render_template('500.html'), 500)
