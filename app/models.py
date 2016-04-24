from app import db


class Rsvps(db.Model):
    __tablename__ = 'rsvps'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    guests = db.Column(db.Integer, index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=False)

    def __init__(self,name,email,guests):
        self.name = name
        self.guests = guests
        self.email = email

    def __repr__(self):
        return 'id: {0}, name: {1}, email: {2}, guests: {3}'.format(
                                                                self.id,
                                                                self.name,
                                                                self.email,
                                                                self.guests
                                                                )

