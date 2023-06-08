from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('mons.config')

db = SQLAlchemy(app)

from mons.views import entries