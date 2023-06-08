from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
import datetime
from holiday.models.mst_holiday import Entry

#初期動作とinput.htmlを読み込む
@app.route('/')
def show_entries():
    entries = Entry.query.all()
    # print(entries)
    return render_template('input.html')

#押されたボタンに応じて処理を実行
@app.route('/entries', methods=['POST'])
def add_entry():
    value = request.form['button']
    entry = Entry(
    holi_date=request.form['date'],
    holi_text=request.form['text']
    )

#     #####
#     print(type(entry.holi_date))
#     print(len(entry.holi_date))
#     print(type(entry.holi_text))
#     print(len(entry.holi_text))
#     #####

#     if entry.holi_date == "":
#          print("naiyo-n")
#     if entry.holi_text == None:
#          print("textmonaiyo-n")
    #エラー処理
    if not(error_flash(entry,value)):
         return redirect(url_for('show_entries'))
    #日付の型を変更
    if (value == "add" or value == "delete")and (entry.holi_date != None):
        entry.holi_date = datetime.datetime.strptime(entry.holi_date,'%Y-%m-%d')
    #追加、更新処理
    if value == "add":
        return update_entry(entry)
        # db.session.merge(entry)
        # db.session.commit()
        # # flash('新しく祝日が登録されました')
        # return render_template('result.html',entry = entry, value = '追加')
    #削除処理
    elif value == "delete":
          return delete_entry(entry)
    #一覧表示処理
    elif value == 'show':
        #   entries = Entry.query.order_by(Entry.holi_date.desc()).all()
          s_en = Entry.query.all()
          return render_template('list.html', entries = s_en)

#エラー判定関数
def error_flash(entry,value):
    if len(entry.holi_date) < 1 and value != 'show':
         flash('日付が入力されていません')
         return False
    if len(entry.holi_text) < 1 and value == 'add':
         flash('テキストが入力されていません')
         return False
    if len(entry.holi_text) > 20:
         flash('テキストは２０文字以内で入力してください')
         return False
    return True

#追加、更新処理
# @app.route('/<int:id>/update', methods=['POST'])
def update_entry(entry):
    al_res = Entry.query.get(entry.holi_date)
#     if al_res == None:
#          print("aiueo")
    db.session.merge(entry)
    db.session.commit()
#     print(al_res)
#     print("122345")
    if al_res == None:
        flash('新しく祝日が登録されました')
        return render_template('result.html',entry = entry, value = '登録')
    else:
        flash('祝日が更新されました')
        return render_template('result.html',entry=entry,value = '更新')

#削除処理
@app.route('/<int:id>/delete', methods=['POST'])
def delete_entry(entry):
    entry_holi_date = Entry.query.get(entry.holi_date)
    if entry_holi_date == None:
         flash('{0}:{1}は祝日として登録されていません'.format(entry.holi_date,entry.holi_text))
         return redirect(url_for('show_entries'))
    db.session.delete(entry_holi_date)
    db.session.commit()
    flash('祝日が削除されました')
    return render_template('result.html',entry=entry_holi_date,value = '削除')
