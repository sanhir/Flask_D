from holiday import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'holidate'
    holi_date = db.Column(db.DateTime, primary_key=True)
    holi_text = db.Column(db.String(20), unique=True)

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return '<Entry date:{} text:{}>'.format( self.date, self.text)