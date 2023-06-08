# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/input',methods = ['POST'])
def entry():
    # 祝日 日付が入力されていたら、値をsessionに保存
    # print(request.form["holiday"])
    # if "holiday" in request.form and "holiday" == request.form["holiday"]:
    #     print(request.form)
    #     session["holiday"]=request.form["holiday"]
    #     print("ああああ"+session["holiday"])
    # else:
    #     flash("祝日 日付が未入力です。日付を選択してください。")
    #     return redirect(url_for('home'))

    # if "holiday" in request.form:
    if request.form["holiday"] == "":
        flash("祝日 日付が未入力です。日付を選択してください。")
        return redirect(url_for('home'))
    else:
        print(request.form)
        session["holiday"]=request.form["holiday"]
        print("ああああ"+session["holiday"])
    # else:
    #     print("ゆなち")
    #     return redirect(url_for('home')) 

    # 新規投稿・更新ボタンを押下されたらinsert_update関数を処理
    if request.form["button"]=="insert_update":
        return insert_update()
    # 削除ボタンを押下されたらdelete_entry関数を処理
    elif request.form["button"]=="delete":
        return delete_entry()
    return render_template('result.html')


# 新規登録・更新ボタンを押下されたらデータベースを更新し、result.htmlを返す
def insert_update():
    entry = Holiday.query.get(session["holiday"])
    if request.form["holiday_text"] == "":
        flash("祝日 テキストを入力してください。")
        return redirect(url_for('home'))
    elif len(request.form["holiday_text"]) > 20:
        flash("祝日 テキストは1-20文字で入力してください。")
        return redirect(url_for('home'))
    # データベースに値があればholi_textをholiday_textに更新する
    elif entry != None:
        entry.holi_text = request.form["holiday_text"]
        db.session.commit()
        info=f"{entry.holi_date}は「{entry.holi_text}」に更新されました"
        return render_template('result.html',infomessage=info)
    # データベースに値がなければholiday_textをテーブルのholi_textに登録する
    else:
        holiday = Holiday(
            holi_date = request.form["holiday"],
            holi_text = request.form["holiday_text"]
        )
        db.session.add(holiday)
        db.session.commit()
        info=f'{request.form["holiday"]}（{request.form["holiday_text"]}）が登録されました'
        return render_template('result.html',infomessage=info)

# 削除ボタンを押下されたら、データベースから値を消去しresult.htmlを出力
def delete_entry():
    # del_date = datetime.date(int(session["holiday"][0:4]), int(session["holiday"][5:7]), int(session["holiday"][8:10]))
    entry = Holiday.query.get(session["holiday"])

    if entry == None:
        flash(f'{session["holiday"]}は、祝日マスタに登録されていません')
        return redirect(url_for('home'))
    else:
        db.session.delete(entry)
        db.session.commit()
        flash("投稿が削除されました")
        info=f"{entry.holi_date}（{entry.holi_text}）は、削除されました"
        return render_template('result.html',infomessage=info)

