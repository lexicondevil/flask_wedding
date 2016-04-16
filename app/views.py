from flask import render_template, flash, redirect
from app import app
from .forms import RsvpForm

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/rsvp/', methods=['GET', 'POST'])
def rsvp():
  form = RsvpForm()
  return render_template('rsvp.html', form=form)

