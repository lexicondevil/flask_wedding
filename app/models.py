from app import db

class Rsvps(db.Model):
    __tablename__ = 'rsvps'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    guests = db.Column(db.Integer, index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self,name,guests,email):
        self.name = name
        self.guests = guests
        self.email = email

