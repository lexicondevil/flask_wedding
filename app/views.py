from flask import render_template, flash, redirect
from app import app, db
from .models import Rsvps
from .forms import RsvpForm

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/rsvp/', methods=['GET', 'POST'])
def rsvp():
  form = RsvpForm(csrf_enabled=True)
  if form.validate_on_submit():
	new_rsvp = Rsvps(
            form.name.data,
            form.email.data,
            form.guests.data
            )
	db.session.add(new_rsvp)
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
