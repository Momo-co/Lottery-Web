from application import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    colour = db.Column(db.String(10), nullable = False)
    number = db.Column(db.Integer, nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    prize = db.Column(db.Integer, nullable = False)