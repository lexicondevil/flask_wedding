from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email

class RsvpForm(Form):
    name = StringField('I.E. Bobby Bottleservice', validators=[InputRequired()])
    email = StringField('Your email here please', validators=[Email()])
    guests = IntegerField('Number of guests in party that will be attending?', validators=[InputRequired()])
    consent = BooleanField('I have read and understood the \'Thanks, but no thanks\' section',\
			   validators=[InputRequired()]) 

#   remember_me = BooleanField('remember_me', default=False)
