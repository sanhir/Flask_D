from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# holidayフォルダ以下のcongfig.pyの内容をconfigとして扱う
app.config.from_object('holiday.config')

db=SQLAlchemy(app)

from holiday.views import maintenance_data,input,list