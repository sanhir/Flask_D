from flask import Flask

app = Flask(__name__)
# holidayフォルダ以下のcongfig.pyの内容をconfigとして扱う
app.config.from_object('holiday.config')

import holiday.views.views