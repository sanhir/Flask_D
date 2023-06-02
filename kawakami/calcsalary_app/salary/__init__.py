from flask import Flask

app = Flask(__name__)
# flask_blogフォルダ以下のcongfig.pyの内容をconfigとして扱う
app.config.from_object('salary.config')

import salary.views.views