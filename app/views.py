from flask import render_template, flash, redirect
from app import app, db
from .models import Rsvps
from .forms import RsvpForm
import time

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
  form = RsvpForm(csrf_enabled=True)
  if form.validate_on_submit():
      newrsvp = Rsvps(
                      form.name.data,
                      form.email.data,
                      form.guests.data
                      )
      db.session.add(newrsvp)
      db.session.commit()
      time.sleep(3)
      flash('Saving your information...')
      return render_template('rsvpeed.html', form=form)
  return render_template('rsvp.html', form=form)

@app.route('/rsvpeed', methods=['GET', 'POST'])
def rsvpeed():
  return render_template('rsvpeed.html') 