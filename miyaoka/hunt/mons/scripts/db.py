from flask_script import Command
from mons import db
from mons.models.entries import Entry


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()