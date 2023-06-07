from holiday import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column('holi_date', db.Date, primary_key = True)
    holi_text = db.Column('holi_text', db.String(20))

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return f'<Holiday holi_date:{self.holi_date} holi_text:{self.holi_text}>'