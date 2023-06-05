# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
from holiday import app


# 最初にinput.htmlを表示する
@app.route('/')
def home():
    return render_template('input.html')

# 新規登録・更新ボタンを押下された
@app.route('/input',methods = 'POST')
def input():
    if request.form["holiday"] == "":
        flash("祝日 日付が未入力です。日付を選択してください。")
        return redirect(url_for('home'))
    elif request.form["holiday_text"] == "" :
        flash("祝日 テキストを入力してください。")
        return redirect(url_for('home'))
    elif len(request.form["holiday_text"]) > 20:
        flash("祝日 テキストは1-20文字で入力してください。")
        return redirect(url_for('home'))
    else:
        return render_template('result.html')
    

# 一覧表示ボタンを押下された
@app.route('/input',methods = 'POST')
def list():
    return render_template('list.html')