from flask import Flask

app = Flask(__name__)
app.config.from_object('flask_salary.config')

import flask_salary.views.views


