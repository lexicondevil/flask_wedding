from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email

class RsvpForm(Form):
    name = StringField('NAME (e.g. Bobby Bottleservice)', validators=[InputRequired()])
    email = StringField('EMAIIL (e.g. HRC_USA@aol.com)', validators=[Email()])
    guests = IntegerField('Number of guests in your party that plan on attending', validators=[InputRequired()])
    consent = BooleanField('I have read and understood the \'Thanks, but no thanks\' section', validators=[InputRequired(message='Sorry, you\'ll have to consent')]) 

#   remember_me = BooleanField('remember_me', default=False)
