from flask import Flask

app = Flask(__name__)
app.config.from_object("flask_calc.config")

import flask_calc.views