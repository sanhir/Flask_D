# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
from holiday import app

# 一覧表示ボタンを押下されたら、list.htmlを返す
@app.route('/list',methods = ['POST'])
def list_entry():
    return render_template('list.html')