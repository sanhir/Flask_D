from mons import db
# from datetime import datetime

class Skill(db.Model):
    __tablename__ = 'skills'
    skill = db.Column(db.String(50),primary_key=True)
    point = db.Column(db.Integer)

    def __init__(self, point=None,skill=None):
        self.skill = skill
        self.point = point
       

    # def __repr__(self):
    #     return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)