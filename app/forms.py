from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email

class RsvpForm(Form):
    rsvp = StringField('Your email here please', \
			 validators=[Email('Please enter a valid email, or you can\'t come to our party!')])
    guests = IntegerField('Number of guests in party that will be attending?', [InputRequired('Need a #')])
    consent = BooleanField('I have read and understood the \'Thanks, but no thanks\' section',\
			   validators=[InputRequired(message='Sorry, you have to agree to the thanks,\
			   but no thanks - it\'s our wedding, sorry!')]) 

#   remember_me = BooleanField('remember_me', default=False)
