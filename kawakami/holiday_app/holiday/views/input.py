# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
from holiday import app

@app.route('/')
def home():
    return render_template('input.html')

# 戻るボタンを押下されたらinput.htmlを返す
@app.route('/back', methods=['POST'])
def back():
    print("あああ")
    return render_template('/input.html')