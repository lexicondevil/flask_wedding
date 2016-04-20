from flask import render_template, flash, redirect
from app import app, db
from .models import Rsvp
from .forms import RsvpForm

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/rsvp/', methods=['GET', 'POST'])
def rsvp():
  form = RsvpForm()
  if form.validate_on_submit():
	rsvp = Rsvp(name=form.name.data, email=form.email.data, guests=form.guests.data)
	db.session.add(rsvp)
	db.session.commit
	#flash('this is a print for {}'.format(rsvp))
  	flash('We\'ve got {} and your +{} all rsvpeed'.format(form.name.data, form.guests.data))
  	flash('Where specifically: Our backyard, 5040 N Oberlin PDX, 97203')
  	flash('When specifically: July 30th, 4pm -> 9pm')
  	flash('Check your {} email address for event information + updates'.format(form.email.data))
  	flash('Questions? Feel free to email/text us!')
  	return render_template('rsvpeed.html', form=form)
  else:
  	return render_template('rsvp.html', form=form)