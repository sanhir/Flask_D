from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# flask_blogフォルダ以下のcongfig.pyの内容をconfigとして扱う
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

import flask_blog.views