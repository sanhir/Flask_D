from mons import db
# from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)
    rarity = db.Column(db.Integer)
    equip = db.Column(db.String(50), unique=True)
    srot = db.Column(db.Integer)
    skill = db.Column(db.String(50))

    def __init__(self, rarity=None,equip=None, srot=None,skill=None):
        self.rarity = rarity
        self.equip = equip
        self.srot = srot
        self.skill = skill
       
class Skill(db.Model):
    __tablename__ = 'skills'
    skill = db.Column(db.String(50),primary_key=True)
    point = db.Column(db.Integer)

    def __init__(self, point=None,skill=None):
        self.skill = skill
        self.point = point
    # def __repr__(self):
    #     return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)