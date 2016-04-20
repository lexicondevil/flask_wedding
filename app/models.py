from app import db

class Rsvp(db.Model):
    __tablename__ = 'rsvp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    guests = db.Column(db.Integer, index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Rsvp %r>' % (self.name)