# -*- coding: utf-8 -*-

from flask import flash, render_template

from app import app
from forms import MyForm


@app.route('/', methods=('GET', 'POST'))
def index():
  form = MyForm()
  if form.validate_on_submit():
    flash('Hey look everyone, he made it!', 'success')
    return render_template('index.html', name=form.name.data)
  return render_template('index.html', form=form)


@app.errorhandler(404)
def error_404(error):
  return (render_template('404.html'), 404)


@app.errorhandler(500)
def error_500(error):
  return (render_template('500.html'), 500)
