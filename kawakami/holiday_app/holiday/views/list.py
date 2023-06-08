# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
from holiday.models.mst_holiday import Holiday

# 一覧表示ボタンを押下されたら、list.htmlを返す
@app.route('/list',methods = ['POST'])
def list_entry():
    # テーブルからすべてのデータを取得
    holidaylist = Holiday.query.all()
    # 取得したデータをlist.htmlの表に挿入
    return render_template('list.html',holidaylist=holidaylist)