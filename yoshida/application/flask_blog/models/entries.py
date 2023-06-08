from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique = True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return '<Entry id:{} title{} text{}>'.format(self.id, self.title, self.text)

class Ojisan(db.Model):
    __tablename__ = "ojisan"
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text)

    def __init__(self, text=None):
        self.text = text
    
    def __repr__(self):
        return '<Entry id:{} text{}>'.format(self.id, self.text)

class ImageURL(db.Model):
    __tablename__ = "imageURL"
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text)

    def __init__(self, url=None):
        self.url = url
    
    def __repr__(self):
        return '<Entry id:{} url{}>'.format(self.id, self.url)